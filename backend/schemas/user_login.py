from pydantic import BaseModel

class userlogin(BaseModel):
    NIC: str
    passcode: str 