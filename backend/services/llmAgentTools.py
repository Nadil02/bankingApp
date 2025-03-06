from models import transaction
from database import collection_transaction
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
    
