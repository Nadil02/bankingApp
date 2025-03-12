from typing import Optional
from schemas.settings import UserNotificationStatus
from database import collection_user


async def get_user_notification_status(user_id: int) -> Optional[UserNotificationStatus]:
    user = await collection_user.find_one({"user_id": user_id})  
    if user:
        return UserNotificationStatus(
            user_id=user["user_id"],
            notification_status=user["notification_status"]
        )
    return None

async def update_user_notification_status(user_id: int, status: bool) -> Optional[UserNotificationStatus]:
    user = await collection_user.find_one({"user_id": user_id})  
    if user:
        await collection_user.update_one(  
            {"user_id": user_id},
            {"$set": {"notification_status": status}}
        )
        return UserNotificationStatus(
            user_id=user["user_id"],
            notification_status=status
        )
    return None
