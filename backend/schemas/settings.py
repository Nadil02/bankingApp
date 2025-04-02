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