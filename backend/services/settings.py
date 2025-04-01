from typing import Optional
from schemas.settings import UserNotificationStatus, UserEditProfile, EditProfileResponse, UserEditProfileWithOTP
from schemas.sign_in import SignInRequest, OtpResponse, SignInResponse
from services.sign_in import sign_in_validation
from database import collection_user, collection_OTP
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

async def load_edit_profile(user_id: int) -> UserEditProfile:
    print("user_id : ",user_id)
    user_details = await collection_user.find_one({"user_id": user_id},{"_id":0,"user_id":1,"first_name":1,"last_name":1,"phone_number":1,"user_image":1})
    
    user_info = {
        "user_id" : user_details["user_id"],
        "fname" : user_details["first_name"],
        "lname" : user_details["last_name"],
        "phone_number" : user_details["phone_number"],
        "user_name" : user_details["first_name"] + "@" + user_details["last_name"],
        "user_image": user_details["user_image"]
    }
    return user_info

async def update_new_details(request: UserEditProfile) -> dict:
    user_tp = request.phone_number
    user_saved_tp = await collection_user.find_one({"user_id": request.user_id},{"_id":0,"phone_number":1})
    if user_tp != user_saved_tp["phone_number"]:
        return EditProfileResponse(message="NeedOTP")
    else:
        #update user details
        await collection_user.update_one(
            {"user_id": request.user_id},
            {"$set": {"first_name": request.fname, "last_name": request.lname}}
        )
        return EditProfileResponse(message="Profile updated successfully")

async def send_sms(p_n: SignInRequest) -> SignInResponse:
    """Send an SMS using Notify.lk API."""
    res = await sign_in_validation(p_n)
    return res

async def validate_otp(otp_request: UserEditProfileWithOTP):
    # check otp existing in the database
    otp_data = await collection_OTP.find_one({"otp_id": otp_request.otp_id, "otp": otp_request.otp})

    #if not existing return error
    if not otp_data:
        return EditProfileResponse(message="Invalid OTP.")
    
    #if existing update the user details
    await collection_user.update_one(
        {"user_id": otp_request.user_id},
        {"$set": {"first_name": otp_request.fname, "last_name": otp_request.lname, "phone_number": otp_request.phone_number}}
    )

    return EditProfileResponse(message="Profile updated successfully.")

