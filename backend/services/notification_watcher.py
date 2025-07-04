from services.websocket_manager import websocket_manager
from database import db, collection_expo_tokens
import httpx
import asyncio
from bson import json_util
import json
from models import NotificationType

EXPO_URL = "https://exp.host/--/api/v2/push/send"

async def send_push_notification(token: str, title: str, body: str, data: dict):
    payload = {
        "to": token,
        "sound": "default",
        "title": title,
        "body": body,
        "data": data,
    }
    async with httpx.AsyncClient() as client:
        try:
            await client.post(EXPO_URL, json=payload)
        except Exception as e:
            print(f"Error sending push notification: {e}")

async def watch_notifications():
    try:
        # Add full_document='updateLookup' to get complete documents
        async with db.notification.watch(
            full_document='updateLookup',
            pipeline=[{
                '$match': {
                    '$or': [
                        {'operationType': 'insert'},
                        {'operationType': 'update'},
                    ]
                }
            }]
        ) as stream:
            async for change in stream:
                # Handle both insert and update cases
                notif = change.get('fullDocument') or change['documentKey']
                if not notif:
                    continue
                    
                # For updates, we may need to fetch the full document
                if isinstance(notif, dict) and '_id' in notif:
                    notif = await db.notification.find_one({"_id": notif["_id"]})
                
                user_id = notif["user_id"]
                notif["_id"] = str(notif["_id"])
                
                await websocket_manager.send_personal_message({
                    "event": "new_notification",
                    "data": notif
                }, user_id)
                
                # Rest of your push notification logic...
    except Exception as e:
        print(f"Watcher error: {str(e)}")
        await asyncio.sleep(5)
        await watch_notifications()