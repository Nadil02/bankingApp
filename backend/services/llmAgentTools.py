# from models import transaction
# from database import collection_transaction

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