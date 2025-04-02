from typing import Optional
from bankingApp.backend.utils.encrypt_and_decrypt import decrypt, encrypt
from schemas.settings import UserNotificationStatus, UserEditProfile, EditProfileResponse, UserEditProfileWithOTP
from schemas.sign_in import SignInRequest, OtpResponse, SignInResponse
from database import collection_user, collection_OTP
from utils.OTP import send_sms
from utils.encrypt_and_decrypt import decrypt, encrypt, decrypt_user_data


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

async def load_edit_profile(user_id: int) -> UserEditProfile:
    print("user_id : ",user_id)
    user_details = await collection_user.find_one({"user_id": user_id},{"_id":0,"user_id":1,"first_name":1,"last_name":1,"phone_number":1,"username":1,"user_image":1})
    
    user_info = {
        #get user information from the database with decrypting the data
        "user_id" : user_details["user_id"],
        "fname" : decrypt(user_details["first_name"]),
        "lname" : decrypt(user_details["last_name"]),
        "phone_number" : decrypt(user_details["phone_number"]),
        "user_name" : decrypt(user_details["username"]),
        "user_image": decrypt(user_details["user_image"])
    }
    return user_info

async def update_new_details(request: UserEditProfile) -> dict:
    userName=encrypt(request.user_name)
    userImage=encrypt(request.user_image)
    await collection_user.update_one(
            {"user_id": request.user_id},
            {"$set": {"username": userName, "user_image": userImage}}
        )
    user_tp = request.phone_number
    user_saved_tp = await collection_user.find_one({"user_id": request.user_id},{"_id":0,"phone_number":1})
    user_tp_number=decrypt(user_saved_tp["phone_number"])
    if user_tp != user_tp_number:
        # send otp to the new number
        pass
    else:
        return EditProfileResponse(message="Profile updated successfully")


