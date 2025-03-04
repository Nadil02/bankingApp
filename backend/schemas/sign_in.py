from pydantic import BaseModel

class SignInRequest(BaseModel):
    phone_number: str

class SignInResponse(BaseModel):
    otp_id: str
    status: str
    message: str

class OtpRequest(BaseModel):
    otp_id: str
    otp: str
    nic: str
    first_name: str
    last_name: str
    phone_number: str
    passcode: str

class OtpResponse(BaseModel):
    status: str
    message: str
    user_id: str