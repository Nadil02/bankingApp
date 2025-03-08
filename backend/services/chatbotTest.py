from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.tools import tool,Tool
import os
from dotenv import load_dotenv
from database import collection_chatbot,collection_transaction,collection_predicted_income,collection_predicted_expense,collection_user,collection_account,collection_predicted_balance
from models import ChatBot,transaction
from datetime import datetime
from langchain_core.tools import StructuredTool
from pydantic import BaseModel
from schemas.chatbot import GetTotalSpendingsArgs,GetTotalIncomeArgs,GetLastTransactionArgs,GetMonthlySummaryArgs,GetAllTransactionsForDateArgs,GetNextMonthTotalIncomesArgs,GetNextMonthTotalSpendingsArgs,GetNextIncomeArgs,GetNextSpendingArgs
from services.llmAgentTools import get_total_spendings_for_given_time_period,get_total_incomes_for_given_time_period,get_last_transaction,get_monthly_summary,get_all_transactions_for_given_date,get_next_month_total_incomes,get_next_month_total_spendings,get_next_income,get_next_spending
# this is original agent
# load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=GEMINI_API_KEY
)


# Define structured tools for all functions
tools = [
     StructuredTool(
        name="get_next_month_total_spendings",
        func=get_next_month_total_spendings,
        description="""Retrieves total spending for the next month.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        
        **Usage Example:**
        If a user asks: *"How much will I spend next month?"*
        The function will be called as:
        ```python
        get_next_month_total_spendings(user_id=12345)
        ```
        The function returns the predicted total spending for the upcoming month.
        """,
        args_schema=GetNextMonthTotalSpendingsArgs,
        coroutine=get_next_month_total_spendings
    )
    ,
    StructuredTool(
        name="get_total_incomes_for_given_time_period",
        func=get_total_incomes_for_given_time_period,
        description="""Retrieves the total income received by a user within a specified time period.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        - `start_date` (datetime, format: YYYY-MM-DD): Start date of the period to analyze.
        - `end_date` (datetime, format: YYYY-MM-DD): End date of the period to analyze.
        
        **Usage Example:**
        If a user asks: *"How much did I earn between January 1, 2024, and January 31, 2024?"*
        The function will be called as:
        ```python
        get_total_incomes_for_given_time_period(
            user_id=12345,
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31)
        )
        ```
        The function returns income amount as a NUMBER. Example: 3500.00
        """,
        args_schema=GetTotalIncomeArgs,
        coroutine=get_total_incomes_for_given_time_period
    ),
    
    StructuredTool(
        name="get_last_transaction",
        func=get_last_transaction,
        description="""Retrieves details about the most recent transaction for a user.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        
        **Usage Example:**
        If a user asks: *"What was my last transaction?"*
        The function will be called as:
        ```python
        get_last_transaction(user_id=12345)
        ```
        The function returns details about the most recent transaction including type, amount, and date.
        """,
        args_schema=GetLastTransactionArgs,
        coroutine=get_last_transaction
    ),
    
    StructuredTool(
        name="get_monthly_summary",
        func=get_monthly_summary,
        description="""Retrieves a summary of financial activity for a specific month.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        - `year` (int): Year for the monthly summary (format: YYYY).
        - `month` (int): Month for the summary (1-12).
        
        **Usage Example:**
        If a user asks: *"What was my financial summary for January 2024?"*
        The function will be called as:
        ```python
        get_monthly_summary(
            user_id=12345,
            year=2024,
            month=1
        )
        ```
        The function returns a summary of total income, expenses, and balance for the specified month.
        """,
        args_schema=GetMonthlySummaryArgs,
        coroutine=get_monthly_summary
    ),
    StructuredTool(
        name="get_all_transactions_for_given_date",
        func=get_all_transactions_for_given_date,
        description="""Retrieves all transactions that occurred on a specific date.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        - `date` (datetime, format: YYYY-MM-DD): Date to retrieve transactions for.
        
        **Usage Example:**
        If a user asks: *"Show me all transactions from January 15, 2024"*
        The function will be called as:
        ```python
        get_all_transactions_for_given_date(
            user_id=12345,
            date=datetime(2024, 1, 15)
        )
        ```
        The function returns a list of all transactions with amounts and descriptions for the specified date.
        """,
        args_schema=GetAllTransactionsForDateArgs,
        coroutine=get_all_transactions_for_given_date
    ),
    StructuredTool(
        name="get_next_month_income",
        func=get_next_month_total_incomes,
        description="""Retrieves total income for the next month. these are predicted values.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        
        **Usage Example:**
        If a user asks: *"How much income can I expect next month?"*
        The function will be called as:
        ```python
        get_next_month_total_incomes(user_id=12345)
        ```
        The function returns the predicted total income for the upcoming month.
        """,
        args_schema=GetNextMonthTotalIncomesArgs,
        coroutine=get_next_month_total_incomes
    ),
    StructuredTool(
        name="get_total_spendings_for_given_time_period",
        func=get_total_spendings_for_given_time_period,
        description="""Retrieves the total amount spent by a user within a specified time period.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        - `start_date` (datetime, format: YYYY-MM-DD): Start date of the period to analyze.
        - `end_date` (datetime, format: YYYY-MM-DD): End date of the period to analyze.
        
        **Usage Example:**
        If a user asks: *"How much did I spend between January 1, 2024, and January 31, 2024?"*
        The function will be called as:
        ```python
        get_total_spendings_for_given_time_period(
            user_id=12345,
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 1, 31)
        )
        ```
        """,
        args_schema=GetTotalSpendingsArgs,
        coroutine=get_total_spendings_for_given_time_period
    ),
    StructuredTool(
        name="get_next_income",
        func=get_next_income,
        description="""Retrieves details about the next predicted income transaction.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        
        **Usage Example:**
        If a user asks: *"When is my next income expected?"*
        The function will be called as:
        ```python
        get_next_income(user_id=12345)
        ```
        The function returns details about the next expected income including date, amount, and description.
        """,
        args_schema=GetNextIncomeArgs,
        coroutine=get_next_income
    ),
     StructuredTool(
        name="get_next_spending",
        func=get_next_spending,
        description="""Retrieves details about the next predicted spending transaction.
        **Parameters:**
        - `user_id` (int): Unique identifier of the user.
        
        **Usage Example:**
        If a user asks: *"What's my next upcoming expense?"*
        The function will be called as:
        ```python
        get_next_spending(user_id=12345)
        ```
        The function returns details about the next expected expense including date, amount, and description.
        """,
        args_schema=GetNextSpendingArgs,
        coroutine=get_next_spending
    )
]

SYSTEM_PROMPT = """You are a financial assistant. Use available tools in sequence when needed.
You can use multiple tools for complex requests. Follow this pattern:
1. Understand the query
2. Identify required tools
3. extract parameters if needed.
4. Use tools sequentially
5. Combine results for final answer"""

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

async def get_chat_summary(user_id: int) -> str:
    user_data =await collection_chatbot.find_one({"user_id": user_id})
    if not user_data:
        new_user = ChatBot(user_id=user_id, chat_summary="")
        await collection_chatbot.insert_one(new_user.dict())
        print("new user added")
        return ""
    return user_data["chat_summary"]


async def update_chat_summary(user_id: int, newSummary: str):
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

async def get_chatbot_response(user_id: int, query: str) -> str:
    
    about_user = await get_chat_summary(user_id)
    
    enriched_query = f"User profile: {about_user}\n\nQuery: {query}\n\nUser ID: {user_id}"
    
    response = await agent_executor.ainvoke({
        "input": enriched_query
    })
    
    new_summary = get_new_summary(query, about_user)
    await update_chat_summary(user_id, new_summary)
    
    return response["output"]