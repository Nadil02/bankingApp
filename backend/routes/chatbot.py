from fastapi import APIRouter, Depends
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbot import get_chatbot_response

router= APIRouter()

@router.post("/chatbot", response_model=ChatbotResponse)
async def chatbot_endpoint(query: ChatbotRequest):
    responseText=await get_chatbot_response(query.user_id, query.query)
    return {"response": responseText}
