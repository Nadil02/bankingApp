from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool
import os
from dotenv import load_dotenv
from database import collection_chatbot
from models import ChatBot

# load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GEMINI_API_KEY
)

# Define tools
@tool
async def get_week_summary(user_id: str) -> str:
    """Returns weekly transaction summary for the user."""
    return "Weekly summary: $1500 income, $900 expenses"

@tool
async def get_month_summary(user_id: str) -> str:
    """Returns monthly transaction summary for the user."""
    return "Monthly summary: $6000 income, $4200 expenses"

tools = [get_week_summary, get_month_summary]
SYSTEM_PROMPT = """You are a financial assistant. Use available tools in sequence when needed.
You can use multiple tools for complex requests. Follow this pattern:
1. Understand the query
2. Identify required tools
3. Use tools sequentially
4. Combine results for final answer"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# create agent
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True,max_iterations=3,handle_parsing_errors=True,early_stopping_method="generate",return_intermediate_steps=False)

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
    
    about_user = await get_chat_summary(user_id)
    
    enriched_query = f"User profile: {about_user}\n\nQuery: {query}\n\nUser ID: {user_id}"
    
    response = await agent_executor.ainvoke({
        "input": enriched_query
    })
    
    new_summary = get_new_summary(query, about_user)
    await update_chat_summary(user_id, new_summary)
    
    return response["output"]