from pydantic import BaseModel
from typing import Optional

class UserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool

class UserEditProfile(BaseModel):
    user_id: int
    fname: str
    lname: str
    phone_number: str
    user_name: str

class UserEditProfileWithOTP(BaseModel):
    otp_id: int
    otp: str
    user_id: int
    fname: str
    lname: str
    phone_number: str
    user_name: str


class EditProfileResponse(BaseModel):
    message: str