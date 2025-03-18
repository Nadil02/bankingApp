from database import collection_account, collection_transaction
from schemas.transaction_history import Dashboard_response, Select_one_account_response

# use this if document need searialization
# def serialize_document(document):
#     document["_id"] = str(document["_id"])
#     return document

async def load_all_accounts(user_id: int) -> dict:
    result = await collection_account.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "account_number": 1, "account_type": 1,"balance": 1}
    ).to_list(length=None)
    return {"accounts " : [Dashboard_response(**item) for item in result]}

async def select_one_account(user_id: int, account_id: int) -> Select_one_account_response:

    pipeline = [
        {"$match": {"account_id": account_id}},  # Filter by account_id
        {
            "$project": {  
                "max_transaction": { "$max": ["$payment", "$receipt"] }  # Find max between payment and receipt
            }
        },
        {
            "$group": {
                "_id": None,
                "max_transaction_value": { "$max": "$max_transaction" }  # Find the max transaction
            }
        }
    ]
    result = await collection_transaction.aggregate(pipeline).to_list(1)  # Get only one result
    max_value = result[0]["max_transaction_value"]
    if result:
        return Select_one_account_response(max_value=max_value)
    else:
        return Select_one_account_response(max_value=None)
    
