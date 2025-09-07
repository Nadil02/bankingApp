from datetime import datetime
from schemas.transaction_categorization import CategoryDetails, Transaction, all_ac_details_response, category_details_response, categorize_transaction_confirmation_response, CategorizeTransactionConfirmationRequest, edit_category_name_request, edit_category_name_response, remove_this_transaction_from_category_response
from database import collection_account, collection_bank, collection_transaction, collection_transaction_category , collection_category_name_changes, collection_transaction_category_changes

async def get_account_details(user_id: int) -> dict:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    accounts = await collection_account.find(
        {"user_id": user_id},
        {"_id": 0, "account_id": 1, "account_number": 1, "account_type": 1, "balance": 1, "bank_id": 1}
    ).to_list(length=None)

    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    print("accounts", accounts)

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
    print("account")
    print("EEEEEEEEEEEEEEEEEEEEEEEEE")

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
            {"category_id": category_id, "account_id": account_id},
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
            {"category_id": category_id, "account_id": account_id},
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

async def categorize_transaction_confirmation(transaction_id: int, previous_category_id: int, new_category_id: int) -> categorize_transaction_confirmation_response:
    # Update the transaction with the new category ID
    result = await collection_transaction.update_one(
        {"transaction_id": transaction_id},
        {"$set": {"category_id": new_category_id}}
    )
    account= await collection_transaction.find_one({"transaction_id": transaction_id}, {"_id": 0, "account_id": 1})
    old_category = await collection_transaction_category.find_one({"category_id": previous_category_id, "account_id": account["account_id"]}) if account else None
    new_category = await collection_transaction_category.find_one({"category_id": new_category_id, "account_id": account["account_id"]}) if account else None

    if result.modified_count > 0:
        txn = await collection_transaction.find_one({"transaction_id": transaction_id})
        await collection_transaction_category_changes.insert_one({
            "transaction_id": transaction_id,
            "account_id": txn.get("description") if txn else "",
            "new_category": new_category,
            "previous_category": old_category,
            "transaction_detail": txn.get("description", "") if txn else "",
            "transaction_date": txn.get("date") if txn else None
        })

    if result.modified_count == 0:
        return categorize_transaction_confirmation_response(
            message="Transaction not found or no changes made",
            transaction_id=transaction_id,
            previous_category_id=previous_category_id,
            new_category_id=new_category_id
        )

    return categorize_transaction_confirmation_response(
        message="Transaction categorized successfully",
        transaction_id=transaction_id,
        previous_category_id=previous_category_id,
        new_category_id=new_category_id
    )

async def edit_category_name(category_id: int, new_category_name: str, account_id: int) -> edit_category_name_response:
    # Update the category name in the database
    old_category = await collection_transaction_category.find_one({"category_id": category_id, "account_id": account_id})
    old_category_name = old_category["category_name"] if old_category else None

    result = await collection_transaction_category.update_one(
        {"category_id": category_id, "account_id": account_id},
        {"$set": {"category_name": new_category_name}}
    )

    if result.modified_count > 0 and old_category_name:
        transactions = await collection_transaction.find({"category_id": category_id}).to_list(length=None)
        for txn in transactions:
            await collection_category_name_changes.insert_one({
                "category_id": category_id,
                "transaction_id": txn["transaction_id"],
                "account_id": txn.get("account_id"),
                "old_category_name": old_category_name,
                "new_category_name": new_category_name,
                "transaction_detail": txn.get("description", ""),
                "transaction_date": txn.get("date")
            })

    if result.modified_count == 0:
        return edit_category_name_response(
            message="Category not found or no changes made",
            category_id=category_id,
            new_category_name=new_category_name
        )

    return edit_category_name_response(
        message="Category name updated successfully",
        category_id=category_id,
        new_category_name=new_category_name
    )

async def remove_this_transaction_from_category(transaction_id: int, category_id: int) -> remove_this_transaction_from_category_response:
    # Update the transaction to remove the category ID
    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    result = await collection_transaction.update_one(
        {"transaction_id": transaction_id},
        {"$set": {"category_id": -1}} #uncategorized -1 
    )
    print("result", result)
    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    account= await collection_transaction.find_one({"transaction_id": transaction_id}, {"_id": 0, "account_id": 1})
    account_id = account["account_id"] if account else None
    old_category = await collection_transaction_category.find_one({"category_id": category_id,"account_id": account_id}) if account_id else None
    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    if result.modified_count > 0:
        txn = await collection_transaction.find_one({"transaction_id": transaction_id})
        print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
        print("txn", txn)
        await collection_transaction_category_changes.insert_one({
            "transaction_id": transaction_id,
            "account_id": txn.get("description") if txn else "",
            "new_category": "Uncategorized",
            "previous_category": old_category,
            "transaction_detail": txn.get("description", "") if txn else "",
            "transaction_date": txn.get("date") if txn else None
        })

    if result.modified_count == 0:
        return remove_this_transaction_from_category_response(
            message="Transaction not found or no changes made",
            transaction_id=transaction_id,
            category_id=category_id
        )

    return remove_this_transaction_from_category_response(
        message="Transaction removed from category successfully",
        transaction_id=transaction_id,
        category_id=category_id
    )