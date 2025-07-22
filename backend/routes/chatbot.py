from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbotTest import get_chatbot_response, get_user_image_service
from services.llmAgentTools import replace_dummy_values, sanizedData, desanizedData
import ast
import re
from utils.auth import verify_token

router= APIRouter(
    # dependencies=[Depends(verify_token)]
)

@router.post("/chatbot")
async def chatbot_endpoint(query: ChatbotRequest):
    print("query :",query.query)
    sanitizedData = await sanizedData(query)  #returns a string
    print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    print("sanitizedData :",sanitizedData)
    responseText=await get_chatbot_response(query.user_id, sanitizedData)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("responseText",responseText)
    responseText=await replace_dummy_values(responseText,query.user_id)
    print("final responseText",responseText)
    # desanitize isuru
    # item = "pay $amount1 to Mr.name1"
    # acutal_values = "{'@amount1': '1000', '@name1': 'john'}"
    # result = await desanizedData(item, acutal_values)
    return {"response" : responseText}

@router.get("/health")
async def health_check():
    return JSONResponse(content={"status": "ok", "message": "Server is running"})

@router.get("/chatbot/user_image")
async def get_user_image(user_id: int):
    return await get_user_image_service(user_id)
