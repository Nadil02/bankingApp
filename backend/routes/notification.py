from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from database import collection_notification, collection_expo_tokens
from schemas.notification import Notification
from models import TokenPayload
from services.websocket_manager import websocket_manager  # Fixed import path
from datetime import datetime
import json

from services.websocket_manager import websocket_manager

router = APIRouter()

@router.websocket("/ws/{user_id}")
async def websocket_notification(websocket: WebSocket, user_id: int):
    await websocket_manager.connect(websocket, user_id)
    try:
        # Send initial notifications
        notifications = await collection_notification.find(
            {"user_id": user_id}
        ).sort("created_at", -1).to_list(length=None)
        
        for notif in notifications:
            notif["_id"] = str(notif["_id"])
        
        await websocket.send_json({
            "event": "initial_notifications",
            "data": notifications
        })
        
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        websocket_manager.disconnect(user_id)
    except Exception as e:
        print(f"WebSocket error: {e}")
        websocket_manager.disconnect(user_id)

@router.post("/create-notification")
async def create_notification(notification: Notification):
    notification_dict = notification.dict()
    notification_dict["created_at"] = datetime.utcnow()
    
    result = await collection_notification.insert_one(notification_dict)
    notification_dict["_id"] = str(result.inserted_id)
    
    # Notify via WebSocket
    await websocket_manager.send_personal_message({
        "event": "new_notification",
        "data": notification_dict
    }, notification.user_id)
    
    return {"status": "success", "notification": notification_dict}

@router.get("/notification/{user_id}")
async def get_all_notifications(user_id: int):
    notifications = await collection_notification.find(
        {"user_id": user_id}
    ).sort("created_at", -1).to_list(length=None)
    
    for notif in notifications:
        notif["_id"] = str(notif["_id"])
    
    return notifications

@router.get("/notification/unread-count/{user_id}")
async def get_unread_notification_count(user_id: int):
    count = await collection_notification.count_documents({
        "user_id": user_id,
        "seen": False
    })
    return {"unread_count": count}

@router.post("/notification/mark-seen/{user_id}")
async def mark_notifications_seen(user_id: int):
    await collection_notification.update_many(
        {"user_id": user_id, "seen": False},
        {"$set": {"seen": True}}
    )
    
    # Notify client via WebSocket
    await websocket_manager.send_personal_message({
        "event": "notifications_seen",
        "data": {"status": "success"}
    }, user_id)
    
    return {"status": "ok"}

@router.post("/save-token")
async def save_token(payload: TokenPayload):
    await collection_expo_tokens.update_one(
        {"user_id": payload.user_id},
        {"$set": {"token": payload.token}},
        upsert=True
    )
    return {"message": "Token saved successfully"}