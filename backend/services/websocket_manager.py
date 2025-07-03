from fastapi import WebSocket
from bson import json_util
import json
from typing import Dict

class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, user_id: int):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    def disconnect(self, user_id: int):
        if user_id in self.active_connections:
            del self.active_connections[user_id]

    async def send_personal_message(self, message: dict, user_id: int):
        if user_id in self.active_connections:
            try:
                # Serialize datetime-safe message using bson
                safe_message = json.loads(json_util.dumps(message))
                await self.active_connections[user_id].send_json(safe_message)
            except Exception as e:
                print(f"WebSocket send error: {e}")
                self.disconnect(user_id)



# Global instance
websocket_manager = WebSocketManager()