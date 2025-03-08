from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from database import collection_chatbot
from models import ChatBot
import json
from services.llmAgentTools import chatbot_system_answer

# import functions from llmAgentTools.py
# from .llmAgentTools import get_week_summary, get_month_summary
from .llmAgentTools import get_total_spendings_for_given_time_period,get_total_incomes_for_given_time_period,get_last_transaction,get_monthly_summary_for_given_month,get_all_transactions_for_given_date,get_next_month_total_incomes,get_next_month_total_spendings,get_next_income,get_next_spending,handle_incomplete_time_periods
from datetime import datetime


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
    {
        "name": "get_total_spendings_for_given_time_period", 
        "func": get_total_spendings_for_given_time_period, 
        "description": "Retrieves the total amount spent by a user within a specified time period. Required parameters: user_id (string), start_date (datetime), end_date (datetime). Use this when the user asks about their spending or expenses for a specific time range."
    },
    {
        "name": "get_total_incomes_for_given_time_period", 
        "func": get_total_incomes_for_given_time_period, 
        "description": "Calculates the total income received by a user within a specified time period. Required parameters: user_id (string), start_date (datetime), end_date (datetime). Use this when the user asks about their income or earnings for a specific time range."
    },
    {
        "name": "get_last_transaction", 
        "func": get_last_transaction, 
        "description": "Retrieves the most recent transaction for a specified user. Required parameters: user_id (string). Use this when the user asks about their latest or most recent transaction."
    },
    {
        "name": "get_monthly_summary_for_given_month", 
        "func": get_monthly_summary_for_given_month, 
        "description": "Provides a summary of total income and spending for a specified month. Required parameters: user_id (string), month (integer 1-12). Use this when the user asks for a financial summary for a specific month."
    },
    {
        "name": "get_all_transactions_for_given_date", 
        "func": get_all_transactions_for_given_date, 
        "description": "Retrieves all transactions that occurred on a specific date for a user. Required parameters: user_id (string), date (datetime). Use this when the user wants to see all transactions from a particular date."
    },
    {
        "name": "get_next_month_total_incomes", 
        "func": get_next_month_total_incomes, 
        "description": "Forecasts the total expected income for the upcoming month based on predicted data. Required parameters: user_id (string). Use this when the user asks about expected or future income for next month."
    },
    {
        "name": "get_next_month_total_spendings", 
        "func": get_next_month_total_spendings, 
        "description": "Forecasts the total expected spending for the upcoming month based on predicted data. Required parameters: user_id (string). Use this when the user asks about expected or future expenses for next month."
    },
    {
        "name": "get_next_income", 
        "func": get_next_income, 
        "description": "Identifies the next expected income transaction based on predicted data. Required parameters: user_id (string). Use this when the user asks when they'll receive their next income or payment."
    },
    {
        "name": "get_next_spending", 
        "func": get_next_spending, 
        "description": "Identifies the next expected expense based on predicted data. Required parameters: user_id (string). Use this when the user asks about their next upcoming expense or bill."
    },
    {
        "name": "handle_incomplete_time_periods", 
        "func": handle_incomplete_time_periods, 
        "description": "Helps manage queries with missing date parameters by prompting for the required information. Required parameters: user_id (string), start_date (datetime, optional), end_date (datetime, optional). Use this when the user's query is missing date information needed for financial analysis."
    },
    {
        "name": "chatbot_system_answer",
        "func": chatbot_system_answer,
        "description": "Use this tool to answer user questions based on system information stored in ChromaDB. Required parameters are user_query (string)"
    }
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

    tool_date_arguments=("Extract the start date and end date from the user query in the format "
    '["YYYY-MM-DD", "YYYY-MM-DD"]. If no date range is provided or required, return an empty array []. '
    "Ensure the extracted dates are valid and properly formatted.")
    
    tool__date_argument_response=llm.invoke(tool_date_arguments).content.strip()
    tool_names = json.loads(tool_response) 
    tool_args = {"user_id": user_id}
    if tool__date_argument_response:
        tool_date=json.loads(tool__date_argument_response)
        if tool_date:  # Ensure it's not an empty array
            start_date = datetime.strptime(tool_date[0], "%Y-%m-%d")
            end_date = datetime.strptime(tool_date[1], "%Y-%m-%d")
            tool_args = {"user_id": user_id, "start_date": start_date, "end_date": end_date}
    tool_results = {}
    


# Assuming tool_date is extracted as a list like ["2022-01-01", "2022-01-31"]
    
    
    
    for tool_name in tool_names:
        for tool in tools:
            if tool['name'] == tool_name:
                tool_results[tool['name']] = tool['func'](**tool_args)

    about_user = await get_chat_summary(user_id)


    final_prompt = f"user query: {query} \n\n about user: {about_user} \n\n tool results: \n{tool_results} "
    final_response = conversation.predict(input=final_prompt)


    await update_chat_summary(user_id, get_new_summary(query,await get_chat_summary(user_id)))

    return final_response

