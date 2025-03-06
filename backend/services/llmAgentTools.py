from models import transaction
from database import collection_transaction,collection_predicted_income,collection_predicted_expense,collection_predicted_balance
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
    total_spendings = collection_transaction.aggregate(
        [
            {"$match": {"user_id": user_id, "date": {"$gte": start_date, "$lte": end_date}}},
            {"$group": {"_id": "$user_id", "total_spendings": {"$sum": "$payment"}}}
        ]
    )
    for i in total_spendings:
        return f"your total spendings are {i['total_spendings']} for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    return "No transactions found"

#create_tool_for_get_total_incomes_for_given_time_period
def get_total_incomes_for_given_time_period(user_id: str, start_date: datetime, end_date: datetime) -> str:
    total_incomes = collection_transaction.aggregate(
        [
            {"$match": {"user_id": user_id, "date": {"$gte": start_date, "$lte": end_date}}},
            {"$group": {"_id": "$user_id", "total_incomes": {"$sum": "$receipt"}}}
        ]
    )
    for i in total_incomes:
        return f"your total incomes are {i['total_incomes']} for the period {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
    return "No transactions found"

#create_tool_for_get_last_transaction
def get_last_transaction(user_id: str) -> str:
    last_transaction = collection_transaction.find_one(
        {"user_id": user_id},
        sort=[("date", -1)]
    )
    if last_transaction:
        txn= transaction(**last_transaction).dict()
        return f"your last transaction was {txn.payment} on {txn.date.strftime('%Y-%m-%d')} description : {txn.description}"
    else:
        return "No transactions found"
    
#create_tool_for_get_monthly_summary_for_given_month
def get_monthly_summary_for_given_month(user_id: str, month: int) -> str:
    monthly_summary = collection_transaction.aggregate(
        [
            {"$match": {"user_id": user_id, "date": {"$month": month}}},
            {"$group": {"_id": "$user_id", "total_incomes": {"$sum": "$receipt"}, "total_spendings": {"$sum": "$payment"}}}
        ]
    )
    for i in monthly_summary:
        return f"your total incomes are {i['total_incomes']} and total spendings are {i['total_spendings']} for the month {month}"
    return "No transactions found"

#create_tool_for_get_all_transactions_for_given_date
def get_all_transactions_for_given_date(user_id: str, date: datetime) -> str:
    transactions = collection_transaction.find(
        {"user_id": user_id, "date": date}
    )
    transactions_list = []
    for txn in transactions:
        transactions_list.append(transaction(**txn).dict())
    if transactions_list:
        return transactions_list
    else:
        return "No transactions found"
    
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
