import json
from bson import json_util
from database import collection_account, collection_bank, collection_user
from schemas.bankAccountManagement import AccountRemove, AccountAdd,BankAccount,RemoveAccountResponse

# get bank account details
async def getBankAccountDetails(user_id: int) -> list[BankAccount]:
    bank_account = await collection_account.find({"user_id": user_id}, {"_id":0,"account_number": 1, "account_type": 1, "balance": 1,"bank_id": 1}).to_list(length=None)
    for bank in bank_account:
        bank_id = bank["bank_id"]
        bank_details = await collection_bank.find_one({"bank_id": bank_id}, {"_id":0,"logo": 1})
        bank.update(bank_details)
        
    bank_account = json.loads(json_util.dumps(bank_account))
    return [BankAccount(**bank) for bank in bank_account]

# check if user exist in the database
async def checkUserExist(user_id: int, nic: str) -> int:
    result = await collection_user.find_one({"nic": nic})
    if result is not None:
        return 1
    else:
        return 0

# remove bank account
async def removeBankAccount(user_id: int, request: AccountRemove):
    # check if the user exist in the database
    if (await checkUserExist(user_id, request.NIC)) == 1:
        user_passcode = await collection_user.find_one({"user_id": user_id}, {"_id":0, "passcode": 1})
        if user_passcode.get("passcode") == request.passcode:
            # find user's bank account and delete it
            result = await collection_account.delete_one({"user_id": user_id, "account_number": request.account_number})
            if result.deleted_count == 0:
                return RemoveAccountResponse(message="Account not found")
            return RemoveAccountResponse(message="success", description="Account removed successfully")
        return RemoveAccountResponse(message = "Passcode is incorrect")
    return RemoveAccountResponse(message= "User not found")
    
# add bank account
async def addBankAccount(user_id: int, request: AccountAdd):
    user_NIC = request.NIC
    #find user exist in the database
    if (await checkUserExist(user_id, user_NIC)) == 1:
        return RemoveAccountResponse(message="success", description="User found")
    else:
        return RemoveAccountResponse(message="Error", description="User not found")
    