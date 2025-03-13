from pydantic import BaseModel

class UserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool

class UserEditProfile(BaseModel):
    user_id: int
    name: str
    phone_number: str
    user_name: str