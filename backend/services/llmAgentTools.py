from models import transaction
from database import collection_transaction,collection_predicted_income,collection_predicted_expense,collection_predicted_balance,collection_user,collection_account
from datetime import datetime



# # def get_last_transaction(user_id: str, account_id: str) -> str:
# #     last_transaction = collection_transaction.find_one(
# #         {"user_id": user_id, "account_id": account_id},
# #         sort=[("date", -1)]
# #     )
# #     if last_transaction:
# #         txn= transaction(**last_transaction).dict()
# #         return f"your last transaction was {txn.payment} on {txn.date.strftime('%Y-%m-%d')} description : {txn.description}"
# #     else:
# #         return "No transactions found"
    
# def get_week_summary(user_id: str) -> str:
#     return "total 1300 incomes were there in the last week"
    
# def get_month_summary(user_id: str) -> str:
#     return "total 2300 incomes were there in the last month"



#create_tool_for_get_total_spendings_for_given_time_period
def get_total_spendings_for_given_time_period(user_id: str, start_date: datetime, end_date: datetime) -> str:
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
    result_list = list(total_spendings_result)
    
    if result_list and "total_spendings" in result_list[0]:
        total_amount = result_list[0]["total_spendings"]
        formatted_start = start_date.strftime('%Y-%m-%d')
        formatted_end = end_date.strftime('%Y-%m-%d')
        return f"Your total spendings are {total_amount:.2f} for the period {formatted_start} to {formatted_end}"
    else:
        return f"No transactions found for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    
#create_tool_for_get_total_incomes_for_given_time_period
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
    



    
#create_too_for_get_next_month_total_incomes
def get_next_month_total_incomes(user_id: str) -> str:
    next_month = datetime.now().month + 1
    next_month_summary = collection_predicted_income.aggregate(
        [
            {"$match": {"user_id": user_id, "date": {"$month": next_month}}},
            {"$group": {"_id": "$user_id", "total_incomes": {"$sum": "$amount"}}}
        ]
    )
    for i in next_month_summary:
        return f"your total incomes for the next month are {i['total_incomes']}"
    return "No transactions found"

#create_tool_for_get_next_month_total_spendings
def get_next_month_total_spendings(user_id: str) -> str:
    next_month = datetime.now().month + 1
    next_month_summary = collection_predicted_expense.aggregate(
        [
            {"$match": {"user_id": user_id, "date": {"$month": next_month}}},
            {"$group": {"_id": "$user_id", "total_spendings": {"$sum": "$amount"}}}
        ]
    )
    for i in next_month_summary:
        return f"your total spendings for the next month are {i['total_spendings']}"
    return "No transactions found"


#create_tool_for_get_next_income
def get_next_income(user_id: str) -> str:
    next_income = collection_predicted_income.find_one(
        {"user_id": user_id},
        sort=[("date", 1)]
    )
    if next_income:
        return f"your next income is {next_income['amount']} on {next_income['date'].strftime('%Y-%m-%d')}"
    else:
        return "No transactions found"
    
#crate_tool_for_the_get_next_spending
def get_next_spending(user_id: str) -> str:
    next_spending = collection_predicted_expense.find_one(
        {"user_id":user_id},
        sort=[("date",1)]
    )
    if next_spending:
        return f"your next income is {next_spending['amount']} on {next_spending['date'].strftime('%Y-%m-%d')}"
    else:
        return "No spending found"


#create_tool_for_handle_incomplete_dates
def handle_incomplete_time_periods(user_id: str, start_date: datetime = None, end_date: datetime = None) -> str:
    if not start_date and not end_date:
        return "Please provide both the start date and end date for the time period."
    elif not start_date:
        return "Please provide the start date for the time period."
    elif not end_date:
        return "Please provide the end date for the time period."
