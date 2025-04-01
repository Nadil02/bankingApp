from schemas.sign_in import SignInRequest, SignInResponse, OtpRequest, OtpResponse
from database import collection_user,collection_OTP
from models import OTP,user
from utils.OTP import send_sms
from utils.encrypt_and_decrypt import encrypt, decrypt_user_data
import random
from argon2 import PasswordHasher
import hashlib
import bcrypt


ph = PasswordHasher()

async def sign_in_validation(sign_in_request: SignInRequest) -> SignInResponse:

    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1  #from 1 if no otp exist

    await storeAndSendOtp(next_otp_id, sign_in_request.phone_number)

    return SignInResponse(otp_id=next_otp_id, status="success", message="otp sent successfully.")

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
    message="hi this is banking app. Your OTP is: "+otp
    send_sms(phone_number, message=message)

async def otp_validation(otp_request: OtpRequest) -> OtpResponse:
    
    otp_data = await collection_OTP.find_one({"otp_id": otp_request.otp_id, "otp": otp_request.otp})
    if not otp_data:
        return OtpResponse(status="error", message="Invalid OTP.", user_id="")
    
    last_user =await collection_user.find_one(sort=[("user_id", -1)])  #  last userid 
    if last_user and "user_id" in last_user:
        next_user_id = last_user["user_id"] + 1
    else:
        next_user_id = 1  #from 1 if no otp exist

    nic_bytes = otp_request.nic.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()

    # print("hashed_nic",hashed_nic)

    salt=bcrypt.gensalt()
    hashed_passcode=bcrypt.hashpw(otp_request.passcode.encode('utf-8'),salt)
    
    user_data = user(
        first_name=encrypt(otp_request.first_name),
        last_name=encrypt(otp_request.last_name),
        username=encrypt(otp_request.first_name),
        NIC=encrypt(otp_request.nic),
        login_nic=hashed_nic,
        phone_number=encrypt(otp_request.phone_number),
        # passcode=ph.hash(otp_request.passcode),
        passcode=hashed_passcode.decode('utf-8'),
        user_id=next_user_id,
        notification_status=True,
    )

    await collection_user.insert_one(user_data.dict(by_alias=True))  #convert user model to dictionary

    return OtpResponse(status="success", message="OTP verified successfully.", user_id=next_user_id)    
        