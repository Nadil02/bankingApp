import json
from bson import json_util
from database import collection_account, collection_bank, collection_user
from models import AccountRemove, AccountAdd

# get bank account details
async def getBankAccountDetails(user_id: int):
    bank_account = await collection_account.find({"user_id": user_id}, {"account_number": 1, "account_type": 1, "balance": 1,"bank_id": 1}).to_list(length=None)
    for bank in bank_account:
        bank_id = bank["bank_id"]
        bank_details = await collection_bank.find_one({"bank_id": bank_id}, {"logo": 1})
        bank.update(bank_details)
    bank_account = json.loads(json_util.dumps(bank_account))
    return {"message": bank_account}

# remove bank account
async def removeBankAccount(user_id: int, request: AccountRemove):
    user_passcode = await collection_user.find_one({"user_id": user_id}, {"passcode": 1})
    if not user_passcode:
        return {"message": "User not found"}
    if user_passcode.get("passcode") == request.passcode:
        # find user's bank account and delete it
        bank_account = await collection_account.find_one({"user_id": user_id, "account_number": request.account_number}, {"bank_id": 1})
        if not bank_account:
            return {"message": "Bank Account not found"}
        await collection_account.delete_one({"user_id": user_id, "account_number": request.account_number})
        # delete bank account from bank collection
        await collection_bank.delete_one({"bank_id": bank_account["bank_id"]}) # This one works properly
        return {"message": "Bank Account Removed"}
    
    return {"message": "Passcode is incorrect"}

# generate otp and validate user
# async def generateOTP(user_id: int):
#     # generate otp
    
# add bank account
async def addBankAccount(user_id: int, request: AccountAdd):
    user_NIC = request.NIC
    #find user exist in the database
    if (await collection_user.find_one({"user_NIC": user_NIC})) is not None:
        return {{"status": "success"}, {"message": "User found"}}
    return {{"status": "Error"}, {"message": "User not found"}}




# bank_account = request.bank_account
#         bank_id = request.bank_id
#         user_id = user_id
#         account_number = request.account_number
#         account_type = request.account_number
#         credit_limit = request.credit_limit
#         due_date = request.due_date
#         balance = request.balance
        
#         # insert bank account to the database
#         result = await collection_account.insert_one({
#             "bank_account": bank_account,
#             "bank_id": bank_id,
#             "user_id": user_id,
#             "account_number": account_number,
#             "account_type": account_type,
#             "credit_limit": credit_limit,
#             "due_date": due_date,
#             "balance": balance
#         })