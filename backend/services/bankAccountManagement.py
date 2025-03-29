import hashlib
import json
import random
import bcrypt
from bson import json_util
from utils.encrypt_and_decrypt import decrypt
from database import collection_account, collection_bank, collection_user, collection_OTP
from schemas.bankAccountManagement import AccountRemove, AccountAdd,BankAccount,RemoveAccountResponse,BankAccountAddResponse,OtpRequestAccountAdding,OtpResponseAccountAdding,OtpRequestAccountAddingResend,OtpResponseAccountAddingResend
from models import OTP, account
from utils.OTP import send_sms
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
    nic_bytes = request.NIC.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(nic_bytes)
    hashed_nic = sha256_hash.hexdigest()

    print("hashed_nic at add bank account",hashed_nic)

    user_data = await collection_user.find_one({"user_id": user_id, "login_nic": hashed_nic})

    if not user_data:
        return BankAccountAddResponse(otp_id=0,status="error", message="entered Nic is wrong.")
    
    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1  #from 1 if no otp exist
    print("user data",user_data)
    user_phone_number = decrypt(user_data["phone_number"])
    print("user_phone_number",user_phone_number)
    # user_phone_number="94710620915"
    await storeAndSendOtp(next_otp_id, user_phone_number)

    return BankAccountAddResponse(otp_id=next_otp_id,status="success", message="otp sent successfully.")

def generate_otp():
    return random.randint(10000, 99999)

async def storeAndSendOtp(next_otp_id: int, phone_number: str):
    otp=str(generate_otp())
    otp_data = OTP(
        otp=otp,
        otp_id=next_otp_id,
        # expiry_time="2025-03-02",
        # verification_count=0 
    )

    await collection_OTP.insert_one(otp_data.dict(by_alias=True))  # Convert OTP model to dictionary
    message="hi this is banking app. Your OTP for add account is: "+otp
    send_sms(phone_number, message=message)

async def otp_validation_account_add(otp_request: OtpRequestAccountAdding) -> OtpResponseAccountAdding:
    
    otp_data = await collection_OTP.find_one({"otp_id": otp_request.otp_id, "otp": otp_request.otp})
    if not otp_data:
        return OtpResponseAccountAdding(status="error", message="Invalid OTP.")
    
    #update bank collection if not exist
    bank= await collection_bank.find_one({"bank_name":otp_request.bank_name})
    if not bank:
        return OtpResponseAccountAdding(status="error", message="bank not found.") 
    else:
        bankId=bank["bank_id"]

    # update bank account collection
    last_account =await collection_account.find_one(sort=[("account_id", -1)])  #  last userid 
    if last_account and "account_id" in last_account:
        next_account_id = last_account["account_id"] + 1
    else:
        next_account_id = 1  #from 1 if no account exist

    
    accountData = account(
        bank_id=bankId,
        account_id=next_account_id,
        user_id=otp_request.user_id,
        account_number=otp_request.account_number,
        account_type=otp_request.account_type,
        credit_limit=0,
        # due_date="",
        balance=0
    )

    await collection_account.insert_one(accountData.dict(by_alias=True))  #convert user model to dictionary

    return OtpResponseAccountAdding(status="success", message="OTP verified and account added successfully.")    

async def resend_otp_account_add(otp_request: OtpRequestAccountAddingResend) -> OtpResponseAccountAdding:
    user_data = await collection_user.find_one({"user_id": otp_request.user_id})  
    last_otp =await collection_OTP.find_one(sort=[("otp_id", -1)])  #  last otpid 
    if last_otp and "otp_id" in last_otp:
        next_otp_id = last_otp["otp_id"] + 1
    else:
        next_otp_id = 1  #from 1 if no otp exist

    user_phone_number = decrypt(user_data["phone_number"])
    print("user_phone_number",user_phone_number)

    await storeAndSendOtp(next_otp_id, user_phone_number)

    return OtpResponseAccountAddingResend(status="success", message="otp sent successfully.")

