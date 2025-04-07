from pydantic import BaseModel

class ChangePasswordRequestSchema(BaseModel):
    user_id: int
    old_password: str
    new_password: str
    confirm_password: str

class ChangePasswordResponseSchema(BaseModel):
    status: str
    message: str
