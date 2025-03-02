from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    user_id: str
    query: str

class ChatbotResponse(BaseModel):
    response: str