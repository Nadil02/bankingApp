from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from database import collection_chatbot
from models import ChatBot
import json

# import functions from llmAgentTools.py
# from .llmAgentTools import get_week_summary, get_month_summary


# get gemini api
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7, google_api_key=GEMINI_API_KEY)

memory = ConversationBufferMemory(memory_keys="chat_history", return_messages=True)
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  
)

#add tools here
tools = [
    # {"name": "get_week_summary", "func": get_week_summary, "description": "Use this tool to get week transaction summary."},
    
]


async def get_chat_summary(user_id: str) -> str:
    user_data =await collection_chatbot.find_one({"user_id": user_id})
    if not user_data:
        new_user = ChatBot(user_id=user_id, chat_summary="")
        await collection_chatbot.insert_one(new_user.dict())
        print("new user added")
        return ""
    return user_data["chat_summary"]


async def update_chat_summary(user_id: str, newSummary: str):
    updated_data = ChatBot(user_id=user_id, chat_summary=newSummary)
    await collection_chatbot.update_one(
        {"user_id": user_id},
        {"$set": updated_data.dict()},
        upsert=True
    )


def get_new_summary(query: str, chat_summary: str) -> str:
    prompt = f"""
    this is the existing financial information summary of user: {chat_summary}
    user query: {query}
    give updated financial information summary for the user using both existing summary and user query.
    financial information can be like favorite day of week, favorite month, lucky number, name etc that 
    can be used to give more personalized responses. if user has no previous summary try to give new one 
    using query data. if conflicts are there in existing summary and query data, give priority to query and 
    generate summary. if not possible to create a summay using query and no exsiting summary is there, 
    then response saying no user summary available. just provide the summary in the response.
    """
    
    new_summary = llm.invoke(prompt)
    
    return new_summary.content.strip()

async def get_chatbot_response(user_id: str, query: str) -> str:

    tool_prompt = f"determine which tools are needed for the following query: {query}\n\nAvailable tools:\n"
    for tool in tools:
        tool_prompt += f"- {tool['name']}: {tool['description']}\n"
    tool_prompt += "\nReturn the tool names in a format of [\"get_week_summary\", \"get_month_summary\"] if get_week_summary and get_month_summary tools are needed. If no tool is needed, the response should be an empty array []"
    tool_response = llm.invoke(tool_prompt).content.strip()

    tool_names = json.loads(tool_response) 
    tool_results = {}
    tool_args = {"user_id": user_id}
    for tool_name in tool_names:
        for tool in tools:
            if tool['name'] == tool_name:
                tool_results[tool['name']] = tool['func'](**tool_args)

    about_user = await get_chat_summary(user_id)


    final_prompt = f"user query: {query} \n\n about user: {about_user} \n\n tool results: \n{tool_results} "
    final_response = conversation.predict(input=final_prompt)


    await update_chat_summary(user_id, get_new_summary(query,await get_chat_summary(user_id)))

    return final_response

