from pydantic import BaseModel

class UserLogin(BaseModel):
    nic: str  # Use lowercase "nic" for consistency with MongoDB field
    passcode: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str
