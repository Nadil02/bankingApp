import json
from ollama import chat
from models import transaction
from database import collection_transaction, collection_predicted_income, collection_predicted_expense, collection_predicted_balance, collection_user, collection_account
from pymongo.errors import PyMongoError
from datetime import datetime
from database import collection_account, collection_transaction, collection_predicted_income, collection_predicted_expense, collection_user, collection_predicted_balance,collection_dummy_values,collection_Todo_list

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
            amount = transaction.get("receipt", transaction.get("payment", 0))
            description = transaction.get("description", "No description")

            transaction_details.append(f"🔹 {transaction_type}: ${amount:.2f} | {description}")

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
            return (
                f" Predicted Total Income for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Income: ${total_predicted_income:.2f} (based on trend and seasonality)"
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
            return (
                f" Predicted Total Spendings for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Spendings: ${total_predicted_spendings:.2f} (based on trend and seasonality)"
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
            date = result["date"].strftime('%Y-%m-%d')
            amount = result["amount"]
            description = result.get("description", "No description available")
            return (
                f" Next Predicted Income: {date}\n"
                f" Amount: ${amount:.2f}\n"
                f" Description: {description}"
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
            date = result["date"].strftime('%Y-%m-%d')
            amount = result["amount"]
            description = result.get("description", "No description available")
            return (
                f" Next Predicted Spending: {date}\n"
                f" Amount: ${amount:.2f}\n"
                f" Description: {description}"
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
    system_prompt = (
        "You are a security assistant. Your task is to identify and redact sensitive financial information in user input. "
        "Extract and store sensitive details in a structured format, and replace those details in the text with placeholders."
        
        "Sensitive details can be: "
        "1. **Monetary amounts** (e.g., '$1000', '5000 dollars', 'USD 300'). Store this under 'amount' and replace it with '@amount'. " 
        "2. **Account numbers** (e.g., '123456789'). Store this under 'accountNumber' and replace it with '@account'. "
        "   Don't keep account numbers like '123456789' in the input field; replace them with '@account'. For example: '123456789' should be replaced with '@account'. "
        "3. **Names** (e.g., 'John', 'Mr. Smith', 'Kasun'). Store this under 'name' and replace it with '@name'. "
        "4. **Dates** (e.g., '2022-01-01', '01/01/2022', '1st January 2022'). Store this under 'date' and replace it with '@date'. "
        "5. **Bank Names** (e.g., 'BOC', 'Sampath', 'Peoples', 'HNB', 'NSB'). Store this under 'account' and replace it with '@bank'. "
        
        "Replace these values **only if they exist in the input**. If no sensitive details are found, return the original input unchanged. "
        "For example : "
        "If user input is 'I need to pay electricity bill', it should return: 'I need to pay electricity bill.' because there is no any sensitive information in the input. "
        "You must handle cases where any or all of these types of sensitive information may be present in the input. "
        
        "Output a JSON object with two fields: "
        "1. **'redacted'**: Contains the sanitized sentence with placeholders. "
        "2. **'original'**: A dictionary containing the extracted sensitive details as key-value pairs. "
        
        "For example: "
        "If a user input contains a monetary amount, such as 'I need to pay $1000 to John.', it should return: "
        "{'redacted': 'I need to pay @amount to @name.', 'original': {'amount': '1000','name': 'John'}}. "
        
        "If a user input contains a bank name, such as 'I have to pay $500 to Sampath bank', it should return: "
        "{'redacted': 'I have to pay @amount to @account bank', 'original': {'amount': '500', account': 'Sampath'}}. "
        
        "Do not keep values in the 'original' field if they are not present in the input. "
        "Return **ONLY** the JSON output. Do not include any metadata, explanations, or additional information in your response."
    )


    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Redact sensitive details from: {user_input}"}
    ]
    response = chat(model='llama3.2:latest', messages=messages)
    content = response['message']['content']
    # llama3.2:3b
    #converting to string 
    content_dict = json.loads(content)
    # taking dummy values
    dummy_values = content_dict["original"]
    # stioring dummy values with actual values in the database
    return_message = await store_dummy_values(user_id, dummy_values)
    print("redacted_string : ",content_dict["redacted"])
    # restoring dummy values with actual values
    # correct_string = await add_to_do_item(user_id, content_dict["redacted"])
    # print("correct_string : ",correct_string)
    return content_dict["redacted"]

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
        if desanitizeValues["date"] is not None:
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
    
