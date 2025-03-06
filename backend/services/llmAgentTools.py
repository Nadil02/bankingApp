
from datetime import datetime
from database import collection_account, collection_transaction

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
