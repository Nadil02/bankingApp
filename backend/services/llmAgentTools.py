from models import transaction
from database import collection_transaction,collection_predicted_income,collection_predicted_expense,collection_predicted_balance,collection_user,collection_account
from datetime import datetime

#create_tool_for_get_total_spendings_for_given_time_period
async def get_total_spendings_for_given_time_period(user_id: str, start_date: datetime, end_date: datetime) -> str:
    # Step 1: Find the user's accounts
    print("inside")
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
        return f"user`s total spendings are ${total_amount} for the period {formatted_start} to {formatted_end} use this and return ${total_amount} were spent by the user in the given time period. here {total_amount} is the amount, add that to the response. "
    else:
        print("No transactions found")
        return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"


def get_total_incomes_for_given_time_period(user_id: str, start_date: datetime, end_date: datetime) -> str:
    # Step 1: Find the user's accounts
    user_accounts = collection_account.find({"user_id": user_id})
    
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
    
    total_incomes_result = collection_transaction.aggregate(pipeline)
    
    # Process the result
    result_list = list(total_incomes_result)
    
    if result_list and "total_incomes" in result_list[0]:
        total_amount = result_list[0]["total_incomes"]
        formatted_start = start_date.strftime('%Y-%m-%d')
        formatted_end = end_date.strftime('%Y-%m-%d')
        return f"Your total incomes are {total_amount:.2f} for the period {formatted_start} to {formatted_end}"
    else:
        return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    
#create_tool_for_get_last_transaction
def get_last_transaction(user_id: str) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Find the most recent transaction
        last_transaction = collection_transaction.find_one(
            {"account_id": {"$in": account_ids}},
            sort=[("date", -1)]  # Sort by date in descending order to get the latest transaction
        )

        if not last_transaction:
            return f"No transactions found for user ID: {user_id}"

        # Extracting details
        transaction_date = last_transaction["date"].strftime('%Y-%m-%d')
        amount = last_transaction.get("receipt", last_transaction.get("expense", 0))
        transaction_type = "Income" if "receipt" in last_transaction else "Expense"

        return f"Last transaction: {transaction_type} of {amount:.2f} on {transaction_date}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
#create_tool_for_get_monthly_summary_for_given_month
def get_monthly_summary(user_id: str, year: int, month: int) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
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
                    "total_expense": {"$sum": {"$ifNull": ["$expense", 0]}}
                }
            }
        ]

        result = next(collection_transaction.aggregate(pipeline), None)

        # Step 4: Format the output
        if result:
            total_income = result.get("total_income", 0)
            total_expense = result.get("total_expense", 0)
            balance = total_income - total_expense
            return (
                f" Monthly Summary for {year}-{month:02d}\n"
                f" Total Income: {total_income:.2f}\n"
                f" Total Expenses: {total_expense:.2f}\n"
                f" Balance: {balance:.2f}"
            )
        else:
            return f"No transactions found for {year}-{month:02d}"

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
#create_tool_for_get_all_transactions_for_given_date
def get_all_transactions_for_given_date(user_id: str, date: datetime) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Query transactions for the given date
        transactions = list(collection_transaction.find(
            {
                "account_id": {"$in": account_ids},
                "date": {"$gte": date, "$lt": date.replace(hour=23, minute=59, second=59)}
            }
        ))

        if not transactions:
            return f"No transactions found for {date.strftime('%Y-%m-%d')}"

        # Step 3: Format the transaction details
        transaction_details = []
        for transaction in transactions:
            transaction_type = "Income" if "receipt" in transaction else "Expense"
            amount = transaction.get("receipt", transaction.get("expense", 0))
            description = transaction.get("description", "No description")

            transaction_details.append(f"🔹 {transaction_type}: {amount:.2f} | {description}")

        formatted_date = date.strftime('%Y-%m-%d')
        return f" Transactions on {formatted_date}:\n" + "\n".join(transaction_details)

    except Exception as e:
        return f"An error occurred: {str(e)}"
    


#prediction_tools.
    
#create_too_for_get_next_month_total_incomes
def get_next_month_total_incomes(user_id: str) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Determine the next month’s date range
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

        result = next(collection_predicted_income.aggregate(pipeline), None)

        # Step 4: Format the response
        if result:
            total_predicted_income = result.get("total_predicted_income", 0)
            return (
                f" Predicted Total Income for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Income: {total_predicted_income:.2f} (based on trend and seasonality)"
            )
        else:
            return f"No predicted incomes found for {next_month_start.strftime('%Y-%m')}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

#create_tool_for_get_next_month_total_spendings
def get_next_month_total_spendings(user_id: str) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
        account_ids = [account["account_id"] for account in user_accounts]

        if not account_ids:
            return f"No accounts found for user ID: {user_id}"

        # Step 2: Determine the next month’s date range
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

        result = next(collection_predicted_expense.aggregate(pipeline), None)

        # Step 4: Format the response
        if result:
            total_predicted_spendings = result.get("total_predicted_spendings", 0)
            return (
                f" Predicted Total Spendings for {next_month_start.strftime('%Y-%m')}\n"
                f" Estimated Spendings: {total_predicted_spendings:.2f} (based on trend and seasonality)"
            )
        else:
            return f"No predicted spendings found for {next_month_start.strftime('%Y-%m')}"

    except Exception as e:
        return f"An error occurred: {str(e)}"


#create_tool_for_get_next_income
def get_next_income(user_id: str) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
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

        result = next(collection_predicted_income.aggregate(pipeline), None)

        # Step 3: Format the response
        if result:
            date = result["date"].strftime('%Y-%m-%d')
            amount = result["amount"]
            description = result.get("description", "No description available")
            return (
                f" Next Predicted Income: {date}\n"
                f" Amount: {amount:.2f}\n"
                f" Description: {description}"
            )
        else:
            return "No upcoming predicted incomes found."

    except Exception as e:
        return f"An error occurred: {str(e)}"
    
#crate_tool_for_the_get_next_spending
def get_next_spending(user_id: str) -> str:
    try:
        # Step 1: Find the user's accounts
        user_accounts = collection_account.find({"user_id": user_id})
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

        result = next(collection_predicted_expense.aggregate(pipeline), None)

        # Step 3: Format the response
        if result:
            date = result["date"].strftime('%Y-%m-%d')
            amount = result["amount"]
            description = result.get("description", "No description available")
            return (
                f" Next Predicted Spending: {date}\n"
                f" Amount: {amount:.2f}\n"
                f" Description: {description}"
            )
        else:
            return "No upcoming predicted spendings found."

    except Exception as e:
        return f"An error occurred: {str(e)}"


#create_tool_for_handle_incomplete_dates
def handle_incomplete_time_periods(user_id: str, start_date: datetime = None, end_date: datetime = None) -> str:
    if not start_date and not end_date:
        return "Please provide both the start date and end date for the time period."
    elif not start_date:
        return "Please provide the start date for the time period."
    elif not end_date:
        return "Please provide the end date for the time period."
