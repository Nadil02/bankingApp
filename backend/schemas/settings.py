from pydantic import BaseModel
from typing import Optional

class updateUserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool
    # name: str
    # user_image: str

class getUserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool
    name: str
    user_image: str
    

class UserEditProfile(BaseModel):
    user_id: int
    phone_number: str
    user_name: str
    user_full_name: str
    user_image: str

class EditProfileResponse(BaseModel):
    message: str
    otp_id: int

class OtpResponseEditTphone(BaseModel):
    status: str
    message: str
    otp_id: int


class OtpRequestEditTphone(BaseModel):
    user_id: int
    otp_id: int 
    otp: str  
    phone_number: str 

class OtpResendRequestEditTphone(BaseModel):
    user_id: int
    otp_id: int 
    phone_number: str  # New phone number to send the OTP to
