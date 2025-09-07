from pydantic import BaseModel
from typing import Optional

class SignInRequest(BaseModel):
    phone_number: str
    nic: str

class SignInResponse(BaseModel):
    otp_id: int
    status: str
    message: str

class OtpRequest(BaseModel):
    otp_id: int 
    otp: str 
    nic: str
    first_name: str 
    last_name: str 
    phone_number: str 
    passcode: str

class OtpResponse(BaseModel):
    status: str
    message: str
    user_id: int

class OtpResendRequest(BaseModel):
    otp_id: int
    phone_number: str

class OtpResendResponse(BaseModel):
    status: str
    message: str
    otp_id: int

class usernameRequest(BaseModel):
    user_id: int

class usernameResponse(BaseModel):
    status: str
    first_name: str
    last_name: str

class pictureUploadRequest(BaseModel):
    user_id: int
    image: str  # Base64 encoded image data

class pictureUploadResponse(BaseModel):
    status: str
    message: str

