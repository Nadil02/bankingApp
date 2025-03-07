from datetime import datetime
from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    user_id: str
    query: str

class ChatbotResponse(BaseModel):
    response: str

class GetTotalSpendingsArgs(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime


class getsystemanswer(BaseModel):
    query: str