from pydantic import BaseModel

class userlogin(BaseModel):
    nic: str
    password: str