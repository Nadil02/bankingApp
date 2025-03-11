import json
import re
from ollama import chat
from models import transaction
from database import collection_transaction, collection_predicted_income, collection_predicted_expense, collection_predicted_balance, collection_user, collection_account
from pymongo.errors import PyMongoError
from datetime import datetime
from database import collection_account, collection_transaction, collection_predicted_income, collection_predicted_expense, collection_user, collection_predicted_balance,collection_dummy_values,collection_Todo_list
import spacy
import json
import re
from nltk.corpus import words  
import nltk

try:
    words.words("en")
except LookupError:
    nltk.download('words')

nlp = spacy.load("en_core_web_sm")


async def get_total_spendings_for_given_time_period(user_id: int, start_date: datetime, end_date: datetime) -> str:
    # Step 1: Find the user's accounts
    print("inside total spendings")

    user_accounts = collection_account.find({"user_id": user_id})
    user_accounts = await user_accounts.to_list(length=None)    
    # Get all account_ids associated with this user
    account_ids = [account["account_id"] for account in user_accounts]
    if not account_ids:
        return f"No accounts found for user ID: {user_id}"
    
    # Step 2: Find transactions for these accounts within the date range
    pipeline = [
        {
            "$match": {
                "account_id": {"$in": account_ids},
                "date": {"$gte": start_date, "$lte": end_date},
                "payment": {"$gt": 0}  # Only count outgoing payments
            }
        },
        {
            "$group": {
                "_id": None,
                "total_spendings": {"$sum": "$payment"}
            }
        }
    ]
    
    total_spendings_result = collection_transaction.aggregate(pipeline)
    
    # Process the result
    # result_list = list(total_spendings_result)
    result_list = await total_spendings_result.to_list(length=None)

    if result_list and "total_spendings" in result_list[0]:
        total_amount = result_list[0]["total_spendings"]
        formatted_start = start_date.strftime('%Y-%m-%d')
        formatted_end = end_date.strftime('%Y-%m-%d')
        print("total_amount",total_amount)
        # return f"user`s total spendings are ${total_amount} for the period {formatted_start} to {formatted_end} use this and return ${total_amount} were spent by the user in the given time period. here {total_amount} is the amount, add that to the response. "
        return f"""{{ 

        "amount": {total_amount}
    }}"""
    else:
        print("No transactions found")
        return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"


async def get_total_incomes_for_given_time_period(user_id: int, start_date: datetime, end_date: datetime) -> str:
    print("inside income")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        
        # Get all account_ids associated with this user
        account_ids = [account["account_id"] for account in user_accounts]
        
        if not account_ids:
            return f"No accounts found for user ID: {user_id}"
        
        # Step 2: Find transactions for these accounts within the date range
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": start_date, "$lte": end_date},
                    "receipt": {"$gt": 0}  # Only count incoming receipts
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_incomes": {"$sum": "$receipt"}
                }
            }
        ]
        
        total_incomes_cursor = collection_transaction.aggregate(pipeline)
        result_list = await total_incomes_cursor.to_list(length=None)
        print("result_list",result_list)
        if result_list and "total_incomes" in result_list[0]:
            total_amount = result_list[0]["total_incomes"]
            formatted_start = start_date.strftime('%Y-%m-%d')
            formatted_end = end_date.strftime('%Y-%m-%d')
            # return f"Your total incomes are ${total_amount:.2f} for the period {formatted_start} to {formatted_end}"
            print("total_amount",total_amount)
            return f"""{{ 
        "amount": {total_amount}
    }}"""
        else:
            return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_last_transaction(user_id: int) -> str:
    print("inside get last transaction")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Find the most recent transaction
        last_transaction = await collection_transaction.find_one(
            {"account_id": {"$in": account_ids}},
            sort=[("date", -1)]  # Sort by date in descending order to get the latest transaction
        )

        if not last_transaction:
            return f"No transactions found for user ID: {user_id}"

        # Extracting details
        transaction_date = last_transaction["date"].strftime('%Y-%m-%d')
        amount = last_transaction.get("receipt", last_transaction.get("payment", 0))
        transaction_type = "Income" if "receipt" in last_transaction else "Expense"

        #return f"Last transaction: {transaction_type} of ${amount:.2f} on {transaction_date}"
        return f"""{{
            "transaction_type": "{transaction_type}",
            "amount": {amount},
        }}"""

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_monthly_summary(user_id: int, year: int, month: int) -> str:
    print("inside get monthly summary")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Define the start and end date of the month
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)  # Start of next year
        else:
            end_date = datetime(year, month + 1, 1)  # Start of next month

        # Step 3: Aggregate transactions for the given month
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": start_date, "$lt": end_date}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_income": {"$sum": {"$ifNull": ["$receipt", 0]}},
                    "total_expense": {"$sum": {"$ifNull": ["$payment", 0]}}
                }
            }
        ]

        aggregate_cursor = collection_transaction.aggregate(pipeline)
        result_list = await aggregate_cursor.to_list(length=None)
        
        # Step 4: Format the output
        if result_list:
            result = result_list[0]
            total_income = result.get("total_income", 0)
            total_expense = result.get("total_expense", 0)
            balance = total_income - total_expense
            return (
                f" Monthly Summary for {year}-{month:02d}\n"
                f" Total Income: ${total_income:.2f}\n"
                f" Total Expenses: ${total_expense:.2f}\n"
                f" Balance: ${balance:.2f}"
            )
        else:
            return f"No transactions found for {year}-{month:02d}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_all_transactions_for_given_date(user_id: int, date: datetime) -> str:
    print("inside get all transactions")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Query transactions for the given date
        end_date = date.replace(hour=23, minute=59, second=59)
        transactions_cursor = collection_transaction.find(
            {
                "account_id": {"$in": account_ids},
                "date": {"$gte": date, "$lte": end_date}
            }
        )
        transactions = await transactions_cursor.to_list(length=None)

        if not transactions:
            return f"No transactions found for {date.strftime('%Y-%m-%d')}"

        # Step 3: Format the transaction details
        transaction_details = []
        for transaction in transactions:

            transaction_type = "Income" if "receipt" in transaction and transaction.get("receipt", 0) > 0 else "Expense"
            dummy_trasaction_type_name = getDummyVariableName(user_id, "@transaction_type")
            StoreResponseDummies(user_id, dummy_trasaction_type_name, transaction_type)
            amount = transaction.get("receipt", transaction.get("payment", 0))
            dummy_amount_name= getDummyVariableName(user_id, "@transaction_amount")
            StoreResponseDummies(user_id, dummy_amount_name, amount)
            description = transaction.get("description", "No description")
            dummy_description_name = getDummyVariableName(user_id, "@transaction_description")
            StoreResponseDummies(user_id, dummy_description_name, description)

            transaction_details.append(f"🔹income or expense : {dummy_trasaction_type_name}: amount : ${dummy_amount_name} | description: {dummy_description_name}")

        formatted_date = date.strftime('%Y-%m-%d')
        return f" Transactions on {formatted_date}:\n" + "\n".join(transaction_details)

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_next_month_total_incomes(user_id: int) -> str:
    print("inside next month total income")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Determine the next month's date range
        today = datetime.today()
        next_month_start = datetime(today.year + (today.month // 12), (today.month % 12) + 1, 1)
        next_month_end = datetime(next_month_start.year + (next_month_start.month // 12), (next_month_start.month % 12) + 1, 1)

        # Step 3: Aggregate predicted incomes from 'predicted_incomes' collection
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": next_month_start, "$lt": next_month_end}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_predicted_income": {"$sum": "$amount"}
                }
            }
        ]

        aggregate_cursor = collection_predicted_income.aggregate(pipeline)
        result_list = await aggregate_cursor.to_list(length=None)

        # Step 4: Format the response
        if result_list:
            total_predicted_income = result_list[0].get("total_predicted_income", 0)

            #sanitize income and store it in dummy variables
            dummy_income_name = getDummyVariableName(user_id, "@predicted_total_income_amount_1")
            StoreResponseDummies(user_id, dummy_income_name, total_predicted_income)

            return (
                f" Predicted Total Income for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Income: ${dummy_income_name} (based on trend and seasonality)"
            )
        else:
            return f"No predicted incomes found for {next_month_start.strftime('%Y-%m')}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_next_month_total_spendings(user_id: str) -> str:
    print("inside next month total spendings")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Determine the next month's date range
        today = datetime.today()
        next_month_start = datetime(today.year + (today.month // 12), (today.month % 12) + 1, 1)
        next_month_end = datetime(next_month_start.year + (next_month_start.month // 12), (next_month_start.month % 12) + 1, 1)

        # Step 3: Aggregate predicted spendings from 'predicted_expenses' collection
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": next_month_start, "$lt": next_month_end}
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total_predicted_spendings": {"$sum": "$amount"}
                }
            }
        ]

        aggregate_cursor = collection_predicted_expense.aggregate(pipeline)
        result_list = await aggregate_cursor.to_list(length=None)

        # Step 4: Format the response
        if result_list:
            total_predicted_spendings = result_list[0].get("total_predicted_spendings", 0)

            #sanitize spendings and store it in dummy variables
            dummy_spendings_name = getDummyVariableName(user_id, "@predicted_total_spendings_amount_1")
            StoreResponseDummies(user_id, dummy_spendings_name, total_predicted_spendings)

            return (
                f" Predicted Total Spendings for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Spendings: ${dummy_spendings_name} (based on trend and seasonality)"
            )
        else:
            return f"No predicted spendings found for {next_month_start.strftime('%Y-%m')}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

async def get_next_income(user_id: int) -> str:
    print("inside next income")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Find the next predicted income (sorted by date)
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": datetime.today()}
                }
            },
            {
                "$sort": {"date": 1}  # Get the nearest future transaction
            },
            {
                "$limit": 1  # Get only the next predicted income
            }
        ]

        aggregate_cursor = collection_predicted_income.aggregate(pipeline)
        result_list = await aggregate_cursor.to_list(length=None)

        # Step 3: Format the response
        if result_list:
            result = result_list[0]
            # Sanitize and store dummy variables for date, amount, and description
            dummy_date_name = getDummyVariableName(user_id, "@predicted_income_date_1")
            StoreResponseDummies(user_id, dummy_date_name, result["date"].strftime('%Y-%m-%d'))
            
            dummy_amount_name = getDummyVariableName(user_id, "@predicted_income_amount_1")
            StoreResponseDummies(user_id, dummy_amount_name, result["amount"])

            dummy_description_name = getDummyVariableName(user_id, "@predicted_income_description_1")
            description = result.get("description", "No description available")
            StoreResponseDummies(user_id, dummy_description_name, description)

            return (
                f" Next Predicted Income: {dummy_date_name}\n"
                f" Amount: ${dummy_amount_name:.2f}\n"
                f" Description: {dummy_description_name}"
            )
        else:
            return "No upcoming predicted incomes found."

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
async def get_next_spending(user_id: int) -> str:
    print("inside next spending")
    try:
        # Step 1: Find the user's accounts
        user_accounts = await collection_account.find({"user_id": user_id}).to_list(length=None)
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Find the next predicted spending (sorted by date)
        pipeline = [
            {
                "$match": {
                    "account_id": {"$in": account_ids},
                    "date": {"$gte": datetime.today()}
                }
            },
            {
                "$sort": {"date": 1}  # Get the nearest future transaction
            },
            {
                "$limit": 1  # Get only the next predicted spending
            }
        ]

        aggregate_cursor = collection_predicted_expense.aggregate(pipeline)
        result_list = await aggregate_cursor.to_list(length=None)

        # Step 3: Format the response
        if result_list:
            result = result_list[0]

            # Sanitize and store dummy variables for date, amount, and description
            dummy_date_name = getDummyVariableName(user_id, "@predicted_spending_date_1")
            StoreResponseDummies(user_id, dummy_date_name, result["date"].strftime('%Y-%m-%d'))

            dummy_amount_name = getDummyVariableName(user_id, "@predicted_spending_amount_1")
            StoreResponseDummies(user_id, dummy_amount_name, result["amount"])

            dummy_description_name = getDummyVariableName(user_id, "@predicted_spending_description_1")
            description = result.get("description", "No description available")
            StoreResponseDummies(user_id, dummy_description_name, description)

            return (
                f" Next Predicted Spending: {dummy_date_name}\n"
                f" Amount: ${dummy_amount_name:.2f}\n"
                f" Description: {dummy_description_name}"
            )
        else:
            return "No upcoming predicted spendings found."

    except Exception as e:
        return f"An error occurred: {str(e)}"

async def handle_incomplete_time_periods(user_id: str, start_date: datetime = None, end_date: datetime = None) -> str:
    
    try:
        if not start_date and not end_date:
            return "Please provide both the start date and end date for the time period."
        elif not start_date:
            return "Please provide the start date for the time period."
        elif not end_date:
            return "Please provide the end date for the time period."
        else:
            # If both dates are provided, return a confirmation message
            return f"Time period from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} is valid."
    except Exception as e:
        return f"An error occurred while processing the time period: {str(e)}"


# creating dummy values for the  user input
async def sanizedData(query: str) -> str:
    """Use the local LLM to detect and redact sensitive information."""
    user_input = query.query
    user_id = query.user_id

#     system_prompt=(
#         """"
#         following are the financial information providing services provided by the system.\n"
#     "1. give transaction history related informations.\n"
#     "2. give total spending amount of user between two given dates.\n"
#     "3. give total incomes of user between two given dates.\n"
#     "4. give the last transaction.\n"
#     "5. give monthly summary of a given month.\n"
        
        
#     You are a highly rule-based banking security assistant. You must strictly follow the instructions below without deviation:

# 1. Your main job is to classify user queries into:
#    - "Not a to-do list task" if they relate to the 5 financial services.
#    - "To-do list task" if they do not relate to any of the 5 financial services.

# 2. If a query has multiple parts, classify each part separately based on the 5 financial services. Use conjunctions ('and', 'or', ',') to split queries logically.

# 3. If any part of the query is a to-do list task and contains amounts, account numbers, names, dates, or bank names, sanitize them as follows:
#    - Replace amounts (e.g., '$1000', '5000 dollars', 'USD 300') with '@amount'.
#    - Replace account numbers (e.g., '123456789') with '@account'.
#    - Replace names (e.g., 'John', 'Mr. Smith', 'Kasun') with '@name'.
#    - Replace dates (e.g., '2022-01-01', '01/01/2022', '1st January 2022', '2022.3.4') with '@date'.
#    - Replace bank names (e.g., 'BOC', 'Sampath', 'Peoples', 'HNB', 'NSB') with '@bank'.

# 4. **Strict Constraints**:
#    - **DO NOT** classify a query as a to-do list task unless it **completely does not match** the 5 financial services.
#    - **DO NOT** sanitize any information unless it is part of a recognized **to-do list task**.
#    - **DO NOT** replace anything other than **amounts, accounts, names, dates, and bank names**.
#    - **DO NOT** assume meanings beyond the given text. If unsure, follow the step-by-step process again.
#    - **DO NOT** make assumptions or generate **example values** in the JSON output.
#    - **DO NOT** provide explanations, metadata, or additional details beyond the required JSON output.
#    -**DO NOT** keep values in the 'original' field if they are not present in the input query.



# 5. **Self-Check Before Finalizing Response:**
#    - Verify if classification aligns with the 5 services.
#    - Ensure no over-sanitization (e.g., replacing words incorrectly).
#    - Ensure no under-sanitization (e.g., missing a name or amount).
#    - If errors are found, correct them before output.

# 6. **Enforced JSON Output Format**:
#    - Output **only** a JSON object with two fields:
#      1. **'redacted'**: Contains the sanitized sentence with placeholders.
#      2. **'original'**: A dictionary containing the extracted sensitive details as key-value pairs.
# - **DO NOT** make assumptions or generate **example values** in the JSON output.
#    - **DO NOT** provide explanations, metadata, or additional details beyond the required JSON output.
#    -**DO NOT** keep values in the 'original' field if they are not present in the input query.


# """
#     )

#     system_prompt=(
#         """"
#        You are a highly rule-based banking security assistant. 
# You must strictly follow the instructions below without deviation. Give quick responses.

# Following is the main financial information providing service provided by the system.

# **Give transaction history related information when asked and answer transaction history related questions.**
# This may include:
# - total spending amount of the user between two given dates,
# - total incomes of the user between two given dates,
# - the last transaction that has been done by the user,
# - monthly summary of a given month of a given year.

      
# 1. Your main job is to classify user queries into:
#    - "Not a to-do list task" if they relate to the main financial service provided by the system.
#    - "To-do list task" if they do not relate to the main financial service provided by the system.

# 2. If a query has multiple parts, you must classify each part separately based on the main financial service provided by the system. Use conjunctions ('and', 'or', ',') to split queries logically.

# 3. If any part of the query is a to-do list task and contains amounts, account numbers, names, dates, or bank names, you must sanitize them as follows:
#    - Replace amounts (e.g., '$1000', '5000 dollars', 'USD 300') with '@amount'. here amount must be a currency related numarical value.
#    - Replace account numbers (e.g., '123456789') with '@account'.
#    - Replace names (e.g., 'John', 'Mr. Smith', 'Kasun') with '@name'.
#    - Replace dates (e.g., '2022-01-01', '01/01/2022', '1st January 2022', '2022.3.4') with '@date'.
#    - Replace bank names (e.g., 'BOC', 'Sampath', 'Peoples', 'HNB', 'NSB') with '@bank'\n.

# 4. **Enforced JSON Output Format:**
#    - Output **only** a single JSON object with two fields:
#      - **'redacted'**: Contains the sanitized sentence with placeholders (if applicable). If no sanitization occurred, include the original query.
#      - **'original'**: A dictionary containing the extracted sensitive details as key-value pairs. 
#        - **DO NOT** keep values in this field if they are not present in the input query.
#        - If no sensitive details are available, include "status": "NA".
#        - For every placeholder used in the 'redacted' field (e.g., @amount, @name, @date, @bank, @account), store the corresponding original value in the 'original' field as key-value pairs.
#        - The 'original' field should never be empty if placeholders exist in 'redacted'.
#    - **DO NOT** make assumptions or generate example values in the JSON output.
#    - Do not provide any additional formatting, explanations, metadata, or code block markers (such as triple backticks).ensure output is a json object that can be directly parsed using json.loads() in Python.
#    - The response must be a plain JSON string that can be directly parsed using json.loads() in Python.

# 5.**Strict Constraints:**
#    - **DO NOT** classify a query as a to-do list task unless it completely does not match the main financial service of the system.
#    - **DO NOT** sanitize any information unless it is part of a recognized to-do list task.
#    - **DO NOT** replace anything other than amounts, accounts, names, dates, and bank names.
#    - **DO NOT** assume meanings beyond the given text. If unsure, follow the step-by-step process again.
#    - Other than sanitizing, you are not allowed to change user query or ask any question from the user.
#    - Strictly follow output instructions.

# 6. **Self-Check these 5 Before Finalizing Response:**
#    1. check and ensure classification is correct and aligns with the main financial service provided by the system.
#    2. check and ensure output is a json object that can be directly parsed using json.loads() in Python.
#    3. check and ensure output is not provide any additional formatting, explanations, metadata, or code block markers (such as triple backticks), classifications. 
#    4. you have successfully sanitized user query and havent done any other changes.
#    5. If errors are found, correct them before output.
# """
#     )

#  If a new query is similar to an example, you **must think it the same way**. Any deviation is strictly prohibited.

# Example 1:
# User Query: "What is my total spending between January 1st, 2024, and February 1st, 2024?"
# Reasoning: The query is asking for the total spending between two dates, which aligns with service #2 (give total spending amount of user between two given dates).
# Classification: Not a to-do list task.
# Sanitized Query: "What is my total spending between January 1st, 2024, and February 1st, 2024?" (No change)
# output :{
#   "redacted": "What is my total spending between @start_date and @end_date?",
#   "original": {
#     "start_date": "January 1st, 2024",
#     "end_date": "February 1st, 2024"
#   }
# }

# Example 2:
# User Query: "Show me my last transaction details."
# Reasoning: The query requests the last transaction details, which falls under service #4 (give the last transaction).
# Classification: Not a to-do list task.
# Sanitized Query: "Show me my last transaction details." (No change)
# output :{
#   "redacted": "Show me my last transaction details.",
#     "original": {}
# }

# Example 3:
# User Query: "Remind me to pay John $5000 next Friday."
# Reasoning: The query is a reminder (to-do list task) and does not match any of the 5 financial services.
# Classification: To-do list task.
# Sanitized Query: "Remind me to pay @name @amount next Friday."
# output :{
#     "redacted": "Remind me to pay @name @amount next Friday.",
#     "original": {
#         "name": "John",
#         "amount": "5000"
#     }

# Example 4:
# User Query: "Schedule a payment to my loan account at Sampath Bank on 15th March 2024."
# Reasoning: The user is asking to schedule a payment, which is a to-do list task. It is unrelated to the 5 services.
# Classification: To-do list task.
# Sanitized Query: "Schedule a payment to my loan account at @bank on @date."
# output :{
#     "redacted": "Schedule a payment to my loan account at @bank on @date.",
#     "original": {
#         "bank": "Sampath Bank",
#         "date": "15th March 2024"
#     }

# Example 5:
# User Query: "Show me my last transaction and remind me to transfer $2000 to Kasun tomorrow."
# Reasoning: - "Show me my last transaction" is a request under service #4 (not a to-do list task).


# "Remind me to transfer $2000 to Kasun tomorrow" is a reminder (to-do list task).
# Classification:

# Not a to-do list task: "Show me my last transaction."
# To-do list task: "Remind me to transfer @amount to @name tomorrow."
# Sanitized Query: "Show me my last transaction and remind me to transfer @amount to @name tomorrow."
# output :{
#     "redacted": "Show me my last transaction and remind me to transfer @amount to @name tomorrow.",
#     "original": {
#         "amount": "2000",
#         "name": "Kasun"
#     }

# Example 6:
# User Query: "What was my total income last month, and remind me to check my NSB account balance next Monday?"
# Reasoning: - "What was my total income last month?" falls under service #3 (not a to-do list task).

# "Remind me to check my NSB account balance next Monday" is a to-do list task.
# Classification:

# Not a to-do list task: "What was my total income last month?"
# To-do list task: "Remind me to check my @bank account balance next Monday."
# Sanitized Query: "What was my total income last month, and remind me to check my @bank account balance next Monday?"
# output :{
#     "redacted": "What was my total income last month, and remind me to check my @bank account balance next Monday?",
#     "original": {
#         "bank": "NSB"
#     }   

# Example 7:
# User Query: "Set a reminder to send $3000 to Mr. Silva on March 10th."
# Sanitized Query: "Set a reminder to send @amount to @name on @date."
# output :{
#     "redacted": "Set a reminder to send @amount to @name on @date.",
#     "original": {
#         "amount": "3000",
#         "name": "Mr. Silva",
#         "date": "March 10th"
#     }

# Example 8:
# User Query: "Remind me to transfer money from account 987654321 to my HNB account on April 5th."
# Sanitized Query: "Remind me to transfer money from account @account to my @bank account on @date."
# output :{
#     "redacted": "Remind me to transfer money from account @account to my @bank account on @date.",
#     "original": {
#         "account": "987654321",
#         "bank": "HNB",
#         "date": "April 5th"
#     }
# }

    # system_prompt = (
    #     "You are a security assistant. Your task is to identify and redact sensitive financial information in user input. \n"
    #     "Extract and store sensitive details in a structured format, and replace those details in the text with placeholders."
        
        # "Sensitive details can be: "
        # "1. **Monetary amounts** (e.g., '$1000', '5000 dollars', 'USD 300'). Store this under 'amount' and replace it with '@amount'. " 
        # "2. **Account numbers** (e.g., '123456789'). Store this under 'accountNumber' and replace it with '@account'. "
        # "   Don't keep account numbers like '123456789' in the input field; replace them with '@account'. For example: '123456789' should be replaced with '@account'. "
        # "3. **Names** (e.g., 'John', 'Mr. Smith', 'Kasun'). Store this under 'name' and replace it with '@name'. "
        # "4. **Dates** (e.g., '2022-01-01', '01/01/2022', '1st January 2022'). Store this under 'date' and replace it with '@date'. "
        # "5. **Bank Names** (e.g., 'BOC', 'Sampath', 'Peoples', 'HNB', 'NSB'). Store this under 'account' and replace it with '@bank'. "
        
    #     "Replace these values **only if they exist in the input**. If no sensitive details are found, return the original input unchanged. "
    #     "For example : "
    #     "If user input is 'I need to pay electricity bill', it should return: 'I need to pay electricity bill.' because there is no any sensitive information in the input. "
    #     "You must handle cases where any or all of these types of sensitive information may be present in the input. "
        
        # "Output a JSON object with two fields: "
        # "1. **'redacted'**: Contains the sanitized sentence with placeholders. "
        # "2. **'original'**: A dictionary containing the extracted sensitive details as key-value pairs. "
        
        # "For example: "
        # "If a user input contains a monetary amount, such as 'I need to pay $1000 to John.', it should return: "
        # "{'redacted': 'I need to pay @amount to @name.', 'original': {'amount': '1000','name': 'John'}}. "
        
        # "If a user input contains a bank name, such as 'I have to pay $500 to Sampath bank', it should return: "
        # "{'redacted': 'I have to pay @amount to @account bank', 'original': {'amount': '500', account': 'Sampath'}}. "
        
    #     "Do not keep values in the 'original' field if they are not present in the input. "
    #     "Return **ONLY** the JSON output. Do not include any metadata, explanations, or additional information in your response."
    # )
    system_prompt = (
        """
        you are a classification assistant. Your task is to classify given user query into one of following two categories quickly:
        - "Not a to-do list task" 
        - "To-do list task" 
        you are not an assitant that answer or work according to the user query.
        you are used to classify user query into one of the above two categories based on the given rules.
        you cannot change following rules.
        you must responde with 1 JSON object with 2 fields "Non to-do list tasks" and "To-do list tasks".
        no any other single words are allowed in the response.
        you must avoid adding code block markers (such as triple backticks).
        you must ensure output is a json object that can be directly parsed using json.loads() in Python.
        if user query has many parts, classify each part separately based on the above two categories. use conjunctions ('and', 'or', ',') to split queries logically.
        add each part of the query or full query into one of the field i the JSON object.
        if a part is seam like possible for both categories, then classify it as "To-do list task".
        you must avoid answer user query and you must classify it or its parts into one of the above two categories using following rules.

        **Rules:**
        1. if user query asking for spendings/expenses or expenses between two given dates, classify it as "Not a to-do list task". this kind of queries contain 2 dates.
        2. if user query asking for income between two given dates, classify it as "Not a to-do list task". this kind of queries contain 2 dates.
        3. if user query asking for the last transaction, classify it as "Not a to-do list task".
        4. if user query asking for monthly summary of a given month/given year and a month, classify it as "Not a to-do list task".
        5. if user query asking for transactions of a given date, classify it as "Not a to-do list task". this kind of queries contain 1 date given.
        6. if user query is not related to any of the above 4 services, classify it as "To-do list task".

        check given user query with above 6 rules and clssify it as "Not a to-do list task" or "To-do list task".
        example :
        "query": "add todo task to ask for a loan"
        response : {"Non to-do list tasks": [], "To-do list tasks": ["add todo task to ask for a loan"]}

        example :
        "query" : "What was my total spending in January and add a task to pay bills."
        response : {"Non to-do list tasks": ["What was my total spending in January"], "To-do list tasks": ["add a task to pay bills"]}

        example :
        "query" : "remind me to pay for john and also give income from 2025.2.3 to 2025.2.6."
        response : {"Non to-do list tasks": ["give income from 2025.2.3 to 2025.2.6"], "To-do list tasks": ["remind me to pay for john"]}
        example :
        "query" : "give me next income and total spending from 2nd of may to 5th of july."
        response : {"Non to-do list tasks": ["give me next income","total spending from 2nd of may to 5th of july"], "To-do list tasks": []}
        example :
        "query" : "remind me to pay for john and kasun. and also give my transaction summary of february."
        response : {"Non to-do list tasks": ["give my transaction summary of february"], "To-do list tasks": ["remind me to pay for john and kasun"]}

        """
        
    )


    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"{user_input}"}
    ]
    response = chat(model='llama3.2:latest', messages=messages)
    content = response['message']['content']
    # llama3.2:3b
    #converting to string 
    print("content : ",content)
    content_dict = json.loads(content)
    non_to_dos=content_dict.get("Non to-do list tasks",[])
    to_dos=content_dict.get("To-do list tasks",[])
    print("non_to_dos : ",non_to_dos)
    print("to_dos : ",to_dos)
    intermediate=orderJson(query.query,content_dict)
    print(intermediate)
    intermediate_ = json.loads(intermediate)
    newJson=dynamic_nlp_sanitize(intermediate_)
    print(newJson)
    # newJson_ = json.loads(newJson)
    # print(newJson_)
    # taking dummy values
    #dummy_values = content_dict["original"]
    dummy_values=newJson["replacements"]
    print("dummy_values : ",dummy_values)
    # stioring dummy values with actual values in the database
    return_message = await store_dummy_values(user_id, dummy_values)
    # print("redacted_string : ",content_dict["redacted"])
    # restoring dummy values with actual values
    # correct_string = await add_to_do_item(user_id, content_dict["redacted"])
    # print("correct_string : ",correct_string)
    # return content_dict["redacted"]
    finalQuery=extract_and_order_tasks(newJson)
    print("finalQuery : ",finalQuery)
    return finalQuery

async def desanizedData(item: str, actual_values: dict) -> dict:
    """Replace dummy values with actual values using the local LLM."""
    
    user_input = item
    print("user_input : ",user_input)
    print("actual_values : ",actual_values)
    system_prompt = (
        "You will receive a prompt containing placeholder values (e.g., '@amount', '@name', '@date', '@bank'). "
        "You will also receive a dictionary with actual values. Your task is to replace the placeholders "
        "with their corresponding values from the dictionary.\n"
        
        "If there are no placeholders in the input, return the input unchanged.\n"
        
        "After replacing placeholders, transform the entire sentence into a usual concise to-do item.\n"
        
        "**Rules:**\n"
        "- Always return a valid **JSON object**.\n"
        "- **Strictly return only the JSON output with no extra text, markdown formatting, or explanations.**\n"
        "- If the input contains '@date' **AND** a corresponding 'date' key exists in the dictionary, store its value under 'date'. **Do not include 'date' in the sentence itself.**\n"
        "- If '@date' is **missing from the sentence OR 'date' does not exist in the dictionary**, **do not include 'date' in the output at all** (do not return 'date': None, 'date': null, or 'date': '').\n"
        "- If no placeholders exist in the sentence, return it as-is under 'sentence'.\n"
        
        "**Examples:**\n"
        "1. Input:\n"
        "   - Prompt: 'I need to pay @amount dollars to @name on @date.'\n"
        "   - Dictionary: {'amount': '500', 'name': 'John', 'date': '2022-01-01'}\n"
        "   - Output:\n"
        "     {\n"
        "       \"sentence\": \"pay 500 to John\",\n"
        "       \"date\": \"2022-01-01\"\n"
        "     }\n"
        
        "2. Input:\n"
        "   - Prompt: 'I need to pay @amount to @name.'\n"
        "   - Dictionary: {'amount': '500', 'name': 'John'}\n"
        "   - Output:\n"
        "     {\n"
        "       \"sentence\": \"pay 500 to John\"\n"
        "     }\n"
        
        "3. Input:\n"
        "   - Prompt: 'I need to pay @amount to @bank bank.'\n"
        "   - Dictionary: {'amount': '500', 'bank': 'BOC'}\n"
        "   - Output:\n"
        "     {\n"
        "       \"sentence\": \"pay 500 to BOC bank\"\n"
        "     }\n"
        
        "4. Input:\n"
        "   - Prompt: 'I need to pay @amount to @bank bank on @date.'\n"
        "   - Dictionary: {'amount': '500', 'bank': 'BOC', 'date': '2025-03-02'}\n"
        "   - Output:\n"
        "     {\n"
        "       \"sentence\": \"pay 500 to BOC bank\",\n"
        "       \"date\": \"2025-03-02\"\n"
        "     }\n"
        
        "5. Input:\n"
        "   - Prompt: 'I need to pay electricity bill.'\n"
        "   - Dictionary: {}\n"
        "   - Output:\n"
        "     {\n"
        "       \"sentence\": \"I need to pay electricity bill.\"\n"
        "     }\n"
    )





    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Replace placeholders in: {user_input} using {json.dumps(actual_values)}"}
    ]

    response = chat(model='llama3.2:latest', messages=messages)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    content = response['message']['content']
    print("content : ",content)
    
    try:
        content = response['message']['content']
        content_dict = json.loads(content)
        print("content_dict : ",content_dict)   
        return content_dict # Return the final replaced text
    except json.JSONDecodeError:
        return {"Error":"Error in desanitization"}  # Return original input in case of an error


#storing dummy values in the dataabase
async def store_dummy_values(user_id:int, dummy_values: dict):
    dummy_dict = {"user_id": user_id}
    dummy_dict.update({key: value for key, value in dummy_values.items() if value is not None})
    try:
        result = await collection_dummy_values.insert_one(dummy_dict)
        return {"success": True, "inserted_id": str(result.inserted_id)}
    except PyMongoError as e:
        return {"success": False, "error": str(e)}

#replace dummy values with actual values
async def add_to_do_item(user_id: int, item: str) -> dict:
    # take dummy values from database
    actual_values = await collection_dummy_values.find_one({"user_id": user_id}, {"_id": 0, "user_id": 0})
    print("actual_values inside add to do item : ",actual_values)
    if actual_values is not None:
        # call another local llm to replace placeholders with actual values
        desanitizeValues = await desanizedData(item, actual_values)
        print("|||||||||||||||||||||||||||||||||||||||||||||||")
        print("desanitizeValues : ",desanitizeValues)
        document = {
            "user_id": user_id,
            "description": desanitizeValues["sentence"],
            "date": None
        }
        if "date" in desanitizeValues and desanitizeValues["date"] is not None:
            document["date"] = desanitizeValues["date"]
        
        try:
            # store the actual values in the database
            result = await collection_Todo_list.insert_one(document)
            # delete dummy values from the database
            await collection_dummy_values.delete_one({"user_id": user_id})
            return {"message":"Successfully added to the to-do list"}
        except PyMongoError as e:
            return {"message": "unable to add list", "error": str(e)}
    
    else:
        return {"message":"No dummy values found for the user"}
    

async def StoreResponseDummies(user_id: int, dummy_name: str, actual_value: any):

    filter_query = {"user_id": user_id}
    existing_doc = await collection_dummy_values.find_one(filter_query)
    
    if not existing_doc:
        new_doc = {"user_id": user_id, dummy_name: actual_value}
        await collection_dummy_values.insert_one(new_doc)
        return "done"
    
    update_query = {"$set": {dummy_name: actual_value}}
    result = await collection_dummy_values.update_one(filter_query, update_query)
    
    return "done" if result.modified_count > 0 else "error"

async def getDummyVariableName(user_id: int, prefix_name: str) -> str:

    filter_query = {"user_id": user_id}
    existing_doc = await collection_dummy_values.find_one(filter_query)
    
    if not existing_doc:
        return f"{prefix_name}_1"
    
    versions = [int(k.split("_")[-1]) for k in existing_doc.keys() if k.startswith(prefix_name) and k.split("_")[-1].isdigit()]
    new_version = max(versions) + 1 if versions else 1
    
    return f"{prefix_name}_{new_version}"

def orderJson(user_query:str,content_dict:dict) -> str:


    cleaned_query = re.sub(r'[^\w\s]', '', user_query).lower().split()
    query_index = {word: idx for idx, word in enumerate(cleaned_query)}

    non_to_dos = {task.lower(): task for task in content_dict.get("Non to-do list tasks", [])}
    to_dos = {task.lower(): task for task in content_dict.get("To-do list tasks", [])}

    # Check for single value case
    if len(non_to_dos) == 1 and len(to_dos) == 0:
        non_to_dos_ordered = {"1": list(non_to_dos.values())[0]}
        to_dos_ordered = {}
        ordered_json = {"Non to-do list tasks": non_to_dos_ordered, "To-do list tasks": to_dos_ordered}
        return json.dumps(ordered_json, indent=4)
    elif len(to_dos) == 1 and len(non_to_dos) == 0:
        to_dos_ordered = {"1": list(to_dos.values())[0]}
        non_to_dos_ordered = {}
        ordered_json = {"Non to-do list tasks": non_to_dos_ordered, "To-do list tasks": to_dos_ordered}
        return json.dumps(ordered_json, indent=4)

    task_positions = {}

    def find_task_index(task, threshold=0.5):  # Threshold defaults to 80%
        task_words = task.lower().split()
        task_len = len(task_words)

        for start_word in range(len(cleaned_query)):
            matched_words = 0
            for i in range(min(task_len, len(cleaned_query) - start_word)):
                if task_words[i] == cleaned_query[start_word + i]:
                    matched_words += 1

            if task_len > 0 and matched_words / task_len >= threshold:
                return start_word

        return float('inf')

    for task_lower, task_original in {**non_to_dos, **to_dos}.items():
        position = find_task_index(task_lower)
        if position != float('inf'):
            task_positions[position] = task_original

    sorted_tasks = sorted(task_positions.items())

    non_to_dos_ordered = {}
    to_dos_ordered = {}
    sentence_index = 1

    for _, task in sorted_tasks:
        if task in non_to_dos.values():
            non_to_dos_ordered[str(sentence_index)] = task
        else:
            to_dos_ordered[str(sentence_index)] = task
        sentence_index += 1

    ordered_json = {"Non to-do list tasks": non_to_dos_ordered, "To-do list tasks": to_dos_ordered}
    return json.dumps(ordered_json, indent=4)

def dynamic_nlp_sanitize(input_json):
    
    entity_types = {
        "MONEY": "@amount",
        "PERSON": "@name",
        "DATE": "@date",
        "ORG": "@bank",
    }

    replacements = {}  
    sanitized_tasks = {} 

    def replace_sensitive(text):
        doc = nlp(text)  
        sanitized_text = text
        entity_occurrences = {} 

        for ent in doc.ents:
            entity_type = entity_types.get(ent.label_)
            if entity_type:
                entity_key = f"{entity_type}{entity_occurrences.get(ent.label_, 0) + 1}"
                if entity_key not in replacements:
                    replacements[entity_key] = ent.text  
                sanitized_text = sanitized_text.replace(ent.text, entity_key)  
                entity_occurrences[ent.label_] = entity_occurrences.get(ent.label_, 0) + 1

        
        account_pattern = r'\b\d{9,}\b'
        for match in re.finditer(account_pattern, sanitized_text):
            account_key = f"@account{len(replacements) + 1}"
            if account_key not in replacements:
                replacements[account_key] = match.group(0)
            sanitized_text = sanitized_text.replace(match.group(0), account_key)

        
        sri_lankan_banks = ["Bank of Ceylon", "Commercial Bank", "Sampath Bank", "HNB", "People's Bank", "NDB", "DFCC Bank"] 
        bank_pattern = r'\b(?:' + '|'.join(re.escape(bank) for bank in sri_lankan_banks) + r')\b'

        for match in re.finditer(bank_pattern, sanitized_text, re.IGNORECASE):
            bank_key = f"@bank{len(replacements) + 1}"
            if bank_key not in replacements:
                replacements[bank_key] = match.group(0)
            sanitized_text = sanitized_text.replace(match.group(0), bank_key)

        return sanitized_text

    
    for key, value in input_json.get("To-do list tasks", {}).items():
        sanitized_tasks[key] = replace_sensitive(value)

    
    def check_non_english_names(sanitized_text):
        words_list = words.words()
        sanitized_text_words = sanitized_text.split()
        potential_names = []
        for word in sanitized_text_words:
            
            if not word.startswith("@") and word.isalpha() and word.lower() not in words_list :
                potential_names.append(word)

        special_words = ["todo"] #words that no need to sanitize
        for name in potential_names:
            if name not in special_words:
                name_key = f"@name{len(replacements) + 1}"
                if name_key not in replacements:
                    replacements[name_key] = name
                sanitized_text = sanitized_text.replace(name, name_key)
        return sanitized_text
        
    for key, value in sanitized_tasks.items():
        sanitized_tasks[key] = check_non_english_names(value)

    
    return {
        "sanitized_data": {
            "Non to-do list tasks": input_json.get("Non to-do list tasks", {}),
            "To-do list tasks": sanitized_tasks
        },
        "replacements": replacements
    }


def extract_and_order_tasks(data):
    try:
        sanitized_data = data.get('sanitized_data', {})
        replacements = data.get('replacements', {})

        def apply_replacements(task_string):
            for placeholder, replacement in replacements.items():
                task_string = task_string.replace(placeholder, replacement)
            return task_string

        ordered_tasks = {}

        for task_type, apply_replacement in [('Non to-do list tasks', True), ('To-do list tasks', False)]:
            tasks = sanitized_data.get(task_type, {})
            for key, task_value in tasks.items():
                ordered_tasks[int(key)] = apply_replacements(task_value) if apply_replacement else task_value

        return ".".join(value for _, value in sorted(ordered_tasks.items()))

    except (json.JSONDecodeError, AttributeError, KeyError, ValueError):
        return ""