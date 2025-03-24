from fastapi import APIRouter, Depends
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbotTest import get_chatbot_response
from services.llmAgentTools import replace_dummy_values, sanizedData, desanizedData
import ast
import re

router= APIRouter()

@router.post("/chatbot")
async def chatbot_endpoint(query: ChatbotRequest):
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
