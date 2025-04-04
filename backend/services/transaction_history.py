from database import collection_account, collection_transaction, collection_credit_periods
from schemas.transaction_history import Dashboard_response, Select_one_account_response, TimeFrameResponse
from datetime import datetime

async def load_all_accounts(user_id: int) -> dict:
    result = await collection_account.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "account_number": 1, "account_type": 1,"balance": 1}
    ).to_list(length=None)
    if len(result) == 0:
        return {"message": "No accounts found"}
    return {"accounts " : [Dashboard_response(**item) for item in result]}

async def select_one_account(user_id: int, account_id: int) -> Select_one_account_response:

    pipeline = [
        {"$match": {"account_id": account_id}},  # Filter by account_id
        {
            "$project": { 
                "max_transaction": { "$max": ["$payment", "$receipt"] },  # Find max between payment and receipt
                "transaction_date": "$date"
            }
        },
        {
            "$group": {
                "_id": None,
                "max_transaction_value": { "$max": "$max_transaction" },  # Find the max transaction
                "first_transaction_date": { "$min": "$transaction_date" }
            }
        }
    ]
    result = await collection_transaction.aggregate(pipeline).to_list(1)  # Get only one result
    max_value = result[0]["max_transaction_value"]
    first_date = result[0]["first_transaction_date"].strftime("%Y-%m-%d")
    if result:
        return Select_one_account_response(max_value=max_value,
            first_transaction_date=first_date)
    else:
        return Select_one_account_response(max_value=None,
            first_transaction_date=None)
    

async def get_transactions_details(account_id: int, start_date: str, end_date: str, range_start: float=None, range_end: float=None, value: float=None):
    # convert date string to datetime object
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):    
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    print("start_date", start_date)
    print("end_date", end_date)

    pipeline = [
        # Match stage to filter by account_id and date range
        {
            "$match": {
                "account_id": account_id,
                "date": {"$gte": start_date, "$lte": end_date},
            }
        },
    ]

    if value is not None:
        pipeline.append({
        "$match": {
            "$or": [
                {"payment": {"$lte": value}}
            ]
        }
        })
    else:
        pipeline.append({
        "$match": {
            "$or": [
                {"payment": {"$gte": range_start, "$lte": range_end}},
                {"receipt": {"$gte": range_start, "$lte": range_end}}
            ]
        }
        })

    pipeline.append({"$sort": {"transaction_date": 1}})
    pipeline.append({"$project": {
                "_id": 0,  # Exclude _id
                "payment": 1,
                "receipt": 1,
                "date": 1,
                "description": 1,
                "balance": 1
            }
        })
    
    result = await collection_transaction.aggregate(pipeline).to_list(None)
    print("result", result)
    return await format_document(result)

#when user select date and range for credit card
async def get_transactions_credit_card_details(user_id:int, account_id: int, time_period:int):
    result_1 = await collection_credit_periods.find_one({"account_id": account_id,"period_id":time_period},{"_id":0, "start_date":1,"end_date":1})
    start_date = result_1["start_date"]
    end_date = result_1["end_date"]
    result_2 = await collection_transaction.find({"account_id": account_id, "date": {"$gte": start_date, "$lte": end_date}}).to_list(length=None)
    return await format_document(result_2)

async def format_document(result):
    formatted_transactions = []

    for txn in result:  # Assuming `db_results` contains the raw database output
        transaction_amount = txn["payment"] if txn["payment"] > 0 else txn["receipt"]
        status = "debit" if txn["payment"] > 0 else "credit"
        formatted_transactions.append({
            "transaction_amount": round(transaction_amount, 2),
            "date": txn["date"].strftime("%Y-%m-%d"),
            "status": status,
            "description": txn["description"],
            "available_balance": round(txn["balance"], 2)})
    formatted_dict = {"transactions": formatted_transactions}
    return formatted_dict
    

async def get_credit_card_timeframes(user_id: int, account_id: int) -> TimeFrameResponse:
    pipeline = [
        {"$match": {"account_id": account_id}},  # Filter by account_id
        {
            "$project": {  
                "period_id": 1,
                "start_date": 1,
                "end_date": 1
            }
        }
    ]
    result = await collection_credit_periods.aggregate(pipeline).to_list(length=None)
    current_period_id = result[-1]["period_id"]
    available_past_time_frames = []
    for item in result:
        if item["period_id"] == current_period_id:
            continue
        available_past_time_frames.append({
            "period_id": item["period_id"],
            "start_date": item["start_date"].strftime("%Y-%m-%d"),
            "end_date": item["end_date"].strftime("%Y-%m-%d")
        })
    current_time_frame = {
        "period_id": current_period_id,
        "start_date": result[-1]["start_date"].strftime("%Y-%m-%d"),
        "end_date": result[-1]["end_date"].strftime("%Y-%m-%d")
    }
    return TimeFrameResponse(available_past_time_frames=available_past_time_frames, current_time_frame=current_time_frame)

