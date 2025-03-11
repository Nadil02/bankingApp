from pydantic import BaseModel

class ForgotPasswordRequestSchema(BaseModel):
    user_id: str
    nic: str
    new_password: str
    confirm_password: str

class ForgotPasswordResponseSchema(BaseModel):
    status: str
    message: str