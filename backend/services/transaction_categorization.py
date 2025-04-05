from datetime import datetime
from schemas.transaction_categorization import CategoryDetails, Transaction, all_ac_details_response, category_details_response
from database import collection_account, collection_bank, collection_transaction, collection_transaction_category

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

async def get_category_details(user_id: int, account_id: int) -> category_details_response:
    #get transactions belong to the account_id from transaction collection
    # seperate those transactions as income and expense using checking payment and reciept fileds of each document and look for non zero field
    # group income and expense categories by category id seperately
    # return json with 2 fields income and expense where each field has caetory name, category id, number of transactions in that category, and list of transactions in that category with transaction id, amount, date, and description
    #  use category collection to get category name and category id using category id from transaction collection

    transactions = await collection_transaction.find(
        {"account_id": account_id},
        {"_id": 0, "transaction_id": 1, "amount": 1, "date": 1, "description": 1, "category_id": 1, "payment": 1, "receipt": 1}
    ).to_list(length=None)
    print(transactions)

    income_transactions = []
    expense_transactions = []
 

    for transaction in transactions:
        if transaction["payment"] > 0:
            expense_transactions.append(transaction)
        elif transaction["receipt"] > 0:
            income_transactions.append(transaction)
    
    print("income_transactions", income_transactions)
    print("expense_transactions", expense_transactions)
    
    income_categories = {}
    expense_categories = {}

    for transaction in income_transactions:
        category_id = transaction["category_id"]

        if category_id not in income_categories:
            category_name = await collection_transaction_category.find_one(
            {"category_id": category_id},
            {"_id": 0, "category_name": 1}
        )
            income_categories[category_id] = {
                "category_id": category_id,
                "category_name": category_name["category_name"] if category_name else "Unknown",
                "transaction_count": 0,
                "transactions": []
            }
        income_categories[category_id]["transaction_count"] += 1
        income_categories[category_id]["transactions"].append({
            "transaction_id": transaction["transaction_id"],
            "amount": transaction["receipt"],
            "date": transaction["date"],
            "description": transaction.get("description", "")
        })

    for transaction in expense_transactions:
        category_id = transaction["category_id"]

        if category_id not in expense_categories:
            category_name = await collection_transaction_category.find_one(
            {"category_id": category_id},
            {"_id": 0, "category_name": 1}
        )
            expense_categories[category_id] = {
                "category_id": category_id,
                "category_name": category_name["category_name"] if category_name else "Unknown",
                "transaction_count": 0,
                "transactions": []
            }
        expense_categories[category_id]["transaction_count"] += 1
        expense_categories[category_id]["transactions"].append({
            "transaction_id": transaction["transaction_id"],
            "amount": transaction["payment"],
            "date": transaction["date"],
            "description": transaction.get("description", "")
        })
    
    income_response = {
        category_id: CategoryDetails(
            category_name=details["category_name"],
            category_id=details["category_id"],
            transaction_count=details["transaction_count"],
            transactions=[
            Transaction(
                transaction_id=txn["transaction_id"],
                amount=txn["amount"],
                date=txn["date"].date() if isinstance(txn["date"], datetime) else txn["date"],  # Convert datetime to date
                description=txn.get("description", "")
            )
            for txn in details["transactions"]
        ]
        )
        for category_id,details in income_categories.items()
    }

    expense_response = {
        category_id: CategoryDetails(
            category_name=details["category_name"],
            category_id=details["category_id"],
            transaction_count=details["transaction_count"],
            transactions=[
            Transaction(
                transaction_id=txn["transaction_id"],
                amount=txn["amount"],
                date=txn["date"].date() if isinstance(txn["date"], datetime) else txn["date"],  # Convert datetime to date
                description=txn.get("description", "")
            )
            for txn in details["transactions"]
        ]
        )
        for category_id,details in expense_categories.items()
    }

    return category_details_response(
        income=income_response,
        expense=expense_response
    )