from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from database import collection_notification, collection_account, collection_expo_tokens
from schemas.notification import Notification
from models import TokenPayload
from services.websocket_manager import websocket_manager
from datetime import datetime
import json

router = APIRouter()

async def get_notifications_with_accounts(user_id: int):
    """Helper function to get notifications with account details"""
    notifications = await collection_notification.find(
        {"user_id": user_id}
    ).sort("created_at", -1).to_list(length=None)
    
    for notif in notifications:
        notif["_id"] = str(notif["_id"])
        if notif.get("account_id"):
            account = await collection_account.find_one({"account_id": notif["account_id"]})
            if account:
                notif.update({
                    "account_number": account["account_number"],
                    "account_type": account["account_type"],
                    "bank_id": account["bank_id"]
                })
    return notifications

@router.websocket("/ws/{user_id}")
async def websocket_notification(websocket: WebSocket, user_id: int):
    await websocket_manager.connect(websocket, user_id)
    try:
        # Initial data with both notifications and unread count
        notifications = await get_notifications_with_accounts(user_id)
        unread_count = await collection_notification.count_documents({
            "user_id": user_id,
            "seen": False
        })
        
        await websocket.send_json({
            "event": "initial_data",
            "data": {
                "notifications": notifications,
                "unread_count": unread_count
            }
        })
        
        # Heartbeat mechanism
        while True:
            data = await websocket.receive_text()
            if data == "ping":
                await websocket.send_text("pong")
                
    except WebSocketDisconnect:
        websocket_manager.disconnect(user_id, websocket)
    except Exception as e:
        print(f"WebSocket error: {e}")
        websocket_manager.disconnect(user_id, websocket)

@router.post("/create-notification")
async def create_notification(notification: Notification):
    notification_dict = notification.dict()
    notification_dict["created_at"] = datetime.utcnow()
    
    # Add account details if exists
    if notification_dict.get("account_id"):
        account = await collection_account.find_one({"account_id": notification_dict["account_id"]})
        if account:
            notification_dict.update({
                "account_number": account["account_number"],
                "account_type": account["account_type"],
                "bank_id": account["bank_id"]
            })
    
    # Insert notification
    result = await collection_notification.insert_one(notification_dict)
    notification_dict["_id"] = str(result.inserted_id)
    
    # Get updated unread count
    unread_count = await collection_notification.count_documents({
        "user_id": notification.user_id,
        "seen": False
    })
    
    # Broadcast to all connected clients
    await websocket_manager.broadcast_to_user(
        notification.user_id,
        {
            "event": "new_notification",
            "data": {
                "notification": notification_dict,
                "unread_count": unread_count
            }
        }
    )
    
    return {"status": "success", "notification": notification_dict}

@router.get("/notification/{user_id}")
async def get_all_notifications(user_id: int):
    return await get_notifications_with_accounts(user_id)

@router.get("/notification/unread-count/{user_id}")
async def get_unread_notification_count(user_id: int):
    count = await collection_notification.count_documents({
        "user_id": user_id,
        "seen": False
    })
    return {"unread_count": count}

@router.post("/notification/mark-seen/{user_id}")
async def mark_notifications_seen(user_id: int):
    # Update all unseen notifications
    await collection_notification.update_many(
        {"user_id": user_id, "seen": False},
        {"$set": {"seen": True}}
    )
    
    # Broadcast to all clients
    await websocket_manager.broadcast_to_user(
        user_id,
        {
            "event": "notifications_seen",
            "data": {
                "status": "success",
                "unread_count": 0  # Explicitly set to 0
            }
        }
    )
    
    return {"status": "ok"}

@router.post("/save-token")
async def save_token(payload: TokenPayload):
    await collection_expo_tokens.update_one(
        {"user_id": payload.user_id},
        {"$set": {"token": payload.token}},
        upsert=True
    )
    return {"message": "Token saved successfully"}