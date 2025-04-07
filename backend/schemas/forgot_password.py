from pydantic import BaseModel

class ForgotPasswordRequestSchema(BaseModel):
    otp_id: int
    otp: str
    nic: str
    new_password: str
    confirm_password: str

class ForgotPasswordResponseSchema(BaseModel):
    status: str
    message: str

class ForgotPasswordOtpRequestSchema(BaseModel):
    nic: str

class ForgotPasswordOtpRequestResponseSchema(BaseModel):
    otp_id: int
    status: str
    message: str

class ForgotPasswordOtpResendRequestSchema(BaseModel):
    otp_id: int
    nic: str

class ForgotPasswordOtpResendResponseSchema(BaseModel):
    otp_id: int
    status: str
    message: str