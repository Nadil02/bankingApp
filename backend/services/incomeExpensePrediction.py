from datetime import datetime, timedelta
from database import collection_account, collection_bank, collection_predicted_income, collection_predicted_expense, collection_transaction_category
from schemas.incomeExpenseprediction import all_ac_details_response_prediction


async def get_account_details_prediction(user_id: int) -> dict:
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

    return {"accounts": [all_ac_details_response_prediction(**account) for account in accounts]}



async def replace_category_ids_with_names(predictions: list[dict]) -> list[dict]:
    for item in predictions:
        category_id = item.get("category_id")
        if category_id is not None:
            category = await collection_transaction_category.find_one(
                {"category_id": category_id},
                {"_id": 0, "category_name": 1}
            )
            item["category_name"] = category["category_name"] if category else "Unknown"
        item.pop("category_id", None)  
    return predictions


async def get_predictions_for_account(user_id: int, account_id: int) -> dict:
    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = today + timedelta(days=31)

    # Fetch and filter by date range
    expense_predictions = await collection_predicted_expense.find(
        {
            "user_id": user_id,
            "account_id": account_id,
            "Date": {"$gte": today, "$lte": end_date}
        },
        {"_id": 0}
    ).to_list(length=None)

    income_predictions = await collection_predicted_income.find(
        {
            "user_id": user_id,
            "account_id": account_id,
            "Date": {"$gte": today, "$lte": end_date}
        },
        {"_id": 0}
    ).to_list(length=None)

    # Add transaction_type
    for item in expense_predictions:
        item["transaction_type"] = "debit"

    for item in income_predictions:
        item["transaction_type"] = "credit"

    # Replace category_id with category_name
    expense_predictions = await replace_category_ids_with_names(expense_predictions)
    income_predictions = await replace_category_ids_with_names(income_predictions)

    return {
        "expenses": expense_predictions,
        "income": income_predictions
    }