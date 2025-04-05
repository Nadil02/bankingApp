from schemas.transaction_categorization import all_ac_details_response
from database import collection_account, collection_bank

async def get_account_details(user_id: int) -> dict:
    accounts = await collection_account.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "account_number": 1, "account_type": 1, "balance": 1, "bank_id": 1}
    ).to_list(length=None)

    if len(accounts) == 0:
        return {"message": "No accounts found"}

    # Fetch bank details for each account
    for account in accounts:
        bank_id = account.get("bank_id")
        if bank_id:
            bank = await collection_bank.find_one(
                {"bank_id": bank_id},
                {"_id": 0, "logo": 1}
            )
            account["image_url"] = bank["logo"] if bank else None
        else:
            account["image_url"] = None

    return {"accounts": [all_ac_details_response(**account) for account in accounts]}