from pydantic import BaseModel

class UserNotificationStatus(BaseModel):
    user_id: int
    notification_status: bool