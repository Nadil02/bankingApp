from typing import Optional
from schemas.settings import UserNotificationStatus, UserEditProfile
from database import collection_user
from utils.OTP import send_sms


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

async def load_edit_profile(user_id: int) -> dict:
    print("user_id : ",user_id)
    user_details = await collection_user.find_one({"user_id": user_id},{"_id":0,"user_id":1,"first_name":1,"last_name":1,"phone_number":1})
    user_info = {
        "user_id" : user_details["user_id"],
        "name" : user_details["first_name"] + " " + user_details["last_name"],
        "phone_number" : user_details["phone_number"],
        "user_name" : user_details["first_name"] + "@" + user_details["last_name"],
    }
    return user_info

async def update_new_details(request: UserEditProfile):
    return {"user_id": "Hello"}

async def send_sms(to: str, message: str):
    """Send an SMS using Notify.lk API."""
    result = send_sms(to, message)

