import hashlib
import random

import bcrypt
from models import OTP
from utils.OTP import send_sms
from utils.encrypt_and_decrypt import decrypt
from database import collection_user, collection_OTP
from schemas.forgot_password import ForgotPasswordOtpRequestResponseSchema, ForgotPasswordOtpRequestSchema, ForgotPasswordOtpResendRequestSchema, ForgotPasswordOtpResendResponseSchema, ForgotPasswordRequestSchema, ForgotPasswordResponseSchema

async def forgot_password_service(request: ForgotPasswordRequestSchema) -> ForgotPasswordResponseSchema:

    otp_data = await collection_OTP.find_one({"otp_id": request.otp_id, "otp": request.otp})
    if not otp_data:
        return ForgotPasswordResponseSchema(status="error", message="Invalid OTP.")
    nic_bytes = request.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()
    print("hashed_nic at forgot password",hashed_nic)
    user_data = await collection_user.find_one({"login_nic": hashed_nic})
    if not user_data:
        return ForgotPasswordResponseSchema(status="error", message="User not found.")
    if request.new_password != request.confirm_password:
        return ForgotPasswordResponseSchema(status="error", message="Passwords do not match.")
    
    #hash password
    salt=bcrypt.gensalt()
    hashed_passcode=bcrypt.hashpw(request.new_password.encode('utf-8'),salt)
    
    await collection_user.update_one({"login_nic": hashed_nic}, {"$set": {"passcode": hashed_passcode.decode('utf-8')}})

    return ForgotPasswordResponseSchema(status="success", message="Password updated successfully.")

async def forgot_password_otp_request_service(request: ForgotPasswordOtpRequestSchema) -> ForgotPasswordOtpRequestResponseSchema:
    print("request",request)
    # Hash the NIC using SHA-256
    nic_bytes = request.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()
    print("hashed_nic at forgot password otp request",hashed_nic)

    # Check if the user exists in the database
    user_data = await collection_user.find_one({"login_nic": hashed_nic})
    print("user_data",user_data)
    if not user_data:
        return ForgotPasswordOtpRequestResponseSchema(otp_id=-1,status="error", message="User not found.")

    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1  #from 1 if no otp exist

    user_phone_number = decrypt(user_data["phone_number"])
    print("user_phone_number",user_phone_number)
    print("next_otp_id",next_otp_id)
    await storeAndSendOtp(next_otp_id, user_phone_number)
    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")

    return ForgotPasswordOtpRequestResponseSchema(otp_id=next_otp_id, status="success", message="OTP sent successfully.")

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
    message="hi this is banking app. Your OTP for forgot password in is: "+otp
    send_sms(phone_number, message=message)

async def forgot_password_otp_resend_request_service(request: ForgotPasswordOtpResendRequestSchema) -> ForgotPasswordOtpResendResponseSchema:
    nic_bytes = request.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()
    print("hashed_nic at forgot password otp resend request",hashed_nic)

    # Check if the user exists in the database
    user_data = await collection_user.find_one({"login_nic": hashed_nic})
    if not user_data:
        return ForgotPasswordOtpResendResponseSchema(otp_id=-1,status="error", message="User not found.")

    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1  #from 1 if no otp exist

    user_phone_number = decrypt(user_data["phone_number"])
    await storeAndSendOtp(next_otp_id, user_phone_number)

    return ForgotPasswordOtpResendResponseSchema(otp_id=next_otp_id, status="success", message="OTP resent successfully.")