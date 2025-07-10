import random
from typing import Optional
from models import OTP
from utils.encrypt_and_decrypt import decrypt, encrypt
from schemas.settings import OtpRequestEditTphone, OtpResendRequestEditTphone, OtpResponseEditTphone, getUserNotificationStatus,updateUserNotificationStatus, UserEditProfile, EditProfileResponse
from schemas.sign_in import SignInRequest, OtpResponse, SignInResponse
from database import collection_user, collection_OTP
from utils.OTP import send_sms
from utils.encrypt_and_decrypt import decrypt, encrypt, decrypt_user_data


async def get_user_notification_status(user_id: int) -> Optional[getUserNotificationStatus]:
    user = await collection_user.find_one({"user_id": user_id})  
    if user:
        # Decrypt the user image
        encrypted_user_image = user["user_image"]
        base64_image = decrypt(encrypted_user_image)

        # Decrypt the first and last name
        user_f_name = user["first_name"]
        user_l_name = user["last_name"]
        user_f_name_dycrypted = decrypt(user_f_name)
        user_l_name_dycrypted = decrypt(user_l_name)
        full_name = user_f_name_dycrypted + " " + user_l_name_dycrypted

        return getUserNotificationStatus(
            user_id=user["user_id"],
            notification_status=user["notification_status"],
            name=full_name,
            user_image=base64_image
        )
    return None

async def update_user_notification_status(user_id: int, status: bool) -> Optional[updateUserNotificationStatus]:
    user = await collection_user.find_one({"user_id": user_id})  
    if user:
        await collection_user.update_one(  
            {"user_id": user_id},
            {"$set": {"notification_status": status}}
        )
        print("******************************************")
        return updateUserNotificationStatus(
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
        "user_full_name" : decrypt(user_details["first_name"]) + " " + decrypt(user_details["last_name"]),
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
    print("user_tp_number : ",user_tp_number)
    print("user_tp : ",user_tp)
    if user_tp != user_tp_number:
        # send otp to the new number
        last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
        if last_otp and "otp_id" in last_otp:
            next_otp_id = last_otp["otp_id"] + 1
            #make next_otp_it_int
            next_otp_id = int(next_otp_id)
        else:
            next_otp_id = int(1) #from 1 if no otp exist

        await storeAndSendOtp(next_otp_id, request.phone_number)
        return EditProfileResponse(message="OTP sent to the new phone number",otp_id=next_otp_id)
    else:
        return EditProfileResponse(message="Profile updated successfully",otp_id=-1)


def generate_otp():
    return random.randint(10000, 99999)

async def storeAndSendOtp(next_otp_id: int, phone_number: str):
    otp=str(generate_otp())
    otp_data = OTP(
        otp=otp,
        otp_id=next_otp_id,
        # expiry_time="2025-03-02",
        # verification_count=0 
    )

    await collection_OTP.insert_one(otp_data.dict(by_alias=True))  # Convert OTP model to dictionary
    message="hi this is banking app. Your OTP for phone number change in is: "+otp
    # send_sms(phone_number, message=message)

async def otp_validation_Tphone_edit(otp_request: OtpRequestEditTphone) -> OtpResponseEditTphone:
        
    otp_data = await collection_OTP.find_one({"otp_id": otp_request.otp_id, "otp": otp_request.otp})
    if not otp_data:
        return OtpResponseEditTphone(status="error", message="Invalid OTP.", otp_id=-1)
    
    new_phone_number = encrypt(otp_request.phone_number)
    await collection_user.update_one(
            {"user_id": otp_request.user_id},
            {"$set": {"phone_number": new_phone_number}}
        )
    return OtpResponseEditTphone(status="success", message="Phone number updated successfully.", otp_id=-1)

async def resend_otp_eidt_Tphone(otp_resend_request: OtpResendRequestEditTphone) -> OtpResponseEditTphone:
    otp_data = await collection_OTP.find_one({"otp_id": otp_resend_request.otp_id})
    if not otp_data:
        return OtpResponseEditTphone(status="error", message="Invalid OTP ID.", otp_id=-1)
    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1
    
    user_phone_number = otp_resend_request.phone_number
    await storeAndSendOtp(next_otp_id, user_phone_number)

    return OtpResponseEditTphone(status="success", message="otp number resent successfully.", otp_id=next_otp_id)