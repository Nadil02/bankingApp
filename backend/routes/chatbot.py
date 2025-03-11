from fastapi import APIRouter, Depends
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbotTest import get_chatbot_response
from services.llmAgentTools import sanizedData

router= APIRouter()

@router.post("/chatbot", response_model=ChatbotResponse)
async def chatbot_endpoint(query: ChatbotRequest):
    sanitizedData = await sanizedData(query)  #returns a string
    print(sanitizedData)
    responseText=await get_chatbot_response(query.user_id, sanitizedData)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("responseText",responseText)
    # desanitize isuru
    return {"response":responseText}
