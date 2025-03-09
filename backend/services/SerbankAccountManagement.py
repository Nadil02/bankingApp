from database import collection_bank, collection_account, collection_user, collection_transaction, collection_predicted_balance, collection_predicted_expense, collection_predicted_income, collection_goal, collection_notification, collection_transaction_category, collection_OTP, collection_Todo_list, collection_chatbot

async def load_bank_accounts_details(user_id: int):
    bank_accounts = []
    async for bank_account in collection_account.find({"user_id": user_id},{"account_number": 1, "balance": 1, "type": 1, "bank_id": 1}):
        bank = await collection_bank.find_one({"_id": bank_account["bank_id"]},{"logo": 1})
        bank_account["bank"] = bank
        bank_accounts.append(bank_account)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("bank_account", bank_account)
    return bank_accounts