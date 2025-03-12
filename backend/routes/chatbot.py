from fastapi import APIRouter, Depends
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbotTest import get_chatbot_response
from services.llmAgentTools import sanizedData, desanizedData
import ast
import re

router= APIRouter()

@router.post("/chatbot")
async def chatbot_endpoint(query: ChatbotRequest):
    sanitizedData = await sanizedData(query)  #returns a string
    print(sanitizedData)
    responseText=await get_chatbot_response(query.user_id, sanitizedData)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("responseText",responseText)
    # desanitize isuru
    # item = "pay $@amount1 to Mr.@name1 and on @date1 at 13.30"
    # acutal_values = "{'@amount1': '1000', '@name1': 'john', '@date1': '15th of March'}"
    # result = await desanizedData(item, acutal_values)
    return {"response" : responseText}
