from fastapi import APIRouter, Depends
from schemas.chatbot import ChatbotRequest, ChatbotResponse
from services.chatbotTest import get_chatbot_response
from services.llmAgentTools import sanizedData, desanizedData
import ast
import re

router= APIRouter()

@router.post("/chatbot")
async def chatbot_endpoint(query: ChatbotRequest):
    # sanitizedData = await sanizedData(query)  #returns a string
    # print(sanitizedData)
    # responseText=await get_chatbot_response(query.user_id, sanitizedData)
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print("responseText",responseText)
    # desanitize isuru
    item = "I need to pay $@amount1 to @name1"
    acutal_values = "{'@amount1': '1000', '@name1': 'john'}"
    # data_dict = ast.literal_eval(acutal_values)

    # def replace_placeholder(match):
    #     return data_dict.get(match.group(0), match.group(0))
    
    # result = re.sub(r'@\w+', replace_placeholder, item)
    # print("result : ", result)

    result = await desanizedData(item, acutal_values)
    return {"response", result}
