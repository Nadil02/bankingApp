from datetime import datetime, timedelta, date
from database import collection_account, collection_bank, collection_predicted_income, collection_predicted_expense, collection_transaction_category, collection_predicted_balance
from schemas.incomeExpenseprediction import all_ac_details_response_prediction
from collections import defaultdict


async def get_account_details_prediction(user_id: int) -> dict:

    accounts = await collection_account.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "account_number": 1, "account_type": 1, "balance": 1, "bank_id": 1}
    ).to_list(length=None)
    print("accounts", accounts)

    if len(accounts) == 0:
        return {"message": "No accounts found"}

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

    for item in expense_predictions:
        item["transaction_type"] = "debit"

    for item in income_predictions:
        item["transaction_type"] = "credit"
    expense_predictions = await replace_category_ids_with_names(expense_predictions)
    income_predictions = await replace_category_ids_with_names(income_predictions)

    return {
        "expenses": expense_predictions,
        "income": income_predictions
    }


async def get_account_balance(user_id: int):

    today = datetime.today().date()
    # today = datetime(2025, 1, 1).date()
    tomorrow = today + timedelta(days=1)
    date_range = [(tomorrow + timedelta(days=i)).isoformat() for i in range(30)]

    # Fetch predicted balances for the user
    predicted_balances = await collection_predicted_balance.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "balance": 1, "date": 1}
    ).to_list(length=None)
    # print("predicted_balances", predicted_balances)

    # Group balance by date
    balance_by_date = defaultdict(float)
    for item in predicted_balances:
        date_obj = item.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            balance_by_date[date_str] += item.get("balance", 0)
    print("balance_by_date", balance_by_date)

    # Get unique account IDs
    account_ids = set(item["account_id"] for item in predicted_balances if "account_id" in item)

    return_dict = {
        "predicted_amounts": []
    }

    total_balance = []
    income_by_date = defaultdict(float)
    expense_by_date = defaultdict(float)

    # Account details
    for account_id in account_ids:
        account_details = await collection_account.find_one(
            {"account_id": account_id},
            {"_id": 0, "account_number": 1, "account_type": 1, "balance": 1}
        )
        # if account_details:
            # total_balance.append(account_details.get("balance", 0))
            # return_dict["account_details"].append({
            #     "account_number": account_details.get("account_number"),
            #     "account_type": account_details.get("account_type"),
            #     "balance": account_details.get("balance"),
            #     "account_id": account_id
            # })

    # Fetch all predicted income docs for the user
    predicted_income_docs = await collection_predicted_income.find(
        {"user_id": user_id},
        {"_id": 0, "date": 1, "amount": 1}
    ).to_list(length=None)
    print("predicted_income_docs", predicted_income_docs)

    for doc in predicted_income_docs:
        date_obj = doc.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            income_by_date[date_str] += doc.get("amount", 0)

    # Fetch all predicted expense docs for the user
    predicted_expense_docs = await collection_predicted_expense.find(
        {"user_id": user_id},
        {"_id": 0, "date": 1, "amount": 1}
    ).to_list(length=None)

    for doc in predicted_expense_docs:
        date_obj = doc.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            expense_by_date[date_str] += doc.get("amount", 0)

    # Compose predicted amounts per date
    for date in date_range:
        return_dict["predicted_amounts"].append({
            "date": date,
            "income": income_by_date.get(date, 0),
            "expense": expense_by_date.get(date, 0),
            "balance": balance_by_date.get(date, 0)
        })
    return return_dict


async def get_specific_account_balance(account_id: int):

    today = datetime.today().date()
    # today = datetime(2025, 1, 1).date()
    tomorrow = today + timedelta(days=1)
    next_30_days = [(tomorrow + timedelta(days=i)).isoformat() for i in range(30)]

    # Fetch balance
    predicted_balance = await collection_predicted_balance.find(
        {"account_id": account_id},
        {"_id": 0, "balance": 1, "date": 1}
    ).to_list(length=None)

    # Fetch income
    predicted_income = await collection_predicted_income.find(
        {"account_id": account_id},
        {"_id": 0, "date": 1, "amount": 1}
    ).to_list(length=None)
    print("predicted_income", predicted_income)

    # Fetch expense
    predicted_expense = await collection_predicted_expense.find(
        {"account_id": account_id},
        {"_id": 0, "date": 1, "amount": 1}
    ).to_list(length=None)

    return_dict = {
        "predicted_amounts": []
    }

    # Group by date
    balance_by_date = defaultdict(float)
    income_by_date = defaultdict(float)
    expense_by_date = defaultdict(float)

    for record in predicted_balance:
        date_obj = record.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            balance_by_date[date_str] = record.get("balance", 0)

    for record in predicted_income:
        date_obj = record.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            income_by_date[date_str] += record.get("amount", 0)

    for record in predicted_expense:
        date_obj = record.get("date")
        if date_obj:
            date_str = date_obj.date().isoformat()
            expense_by_date[date_str] += record.get("amount", 0)

    # Combine into result
    for date in next_30_days:
        return_dict["predicted_amounts"].append({
            "date": date,
            "balance": balance_by_date.get(date, 0),
            "income": income_by_date.get(date, 0),
            "expense": expense_by_date.get(date, 0)
        })

    return return_dict




