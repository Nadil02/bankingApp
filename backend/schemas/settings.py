from pydantic import BaseModel
from typing import Optional

class UserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool

class UserEditProfile(BaseModel):
    user_id: int
    phone_number: str
    user_name: str
    user_image: str
class EditProfileResponse(BaseModel):
    message: str

class OtpResponseEditTphone(BaseModel):
    status: str
    message: str


class OtpRequestEditTphone(BaseModel):
    user_id: int
    otp_id: int 
    otp: str  
    phone_number: str 

class OtpResendRequestEditTphone(BaseModel):
    user_id: int
    otp_id: int 
    phone_number: str  # New phone number to send the OTP to
