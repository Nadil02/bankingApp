from fastapi import APIRouter
from services.bankAccountManagement import getBankAccountDetails, removeBankAccount, addBankAccount
from schemas.bankAccountManagement import AccountRemove, AccountAdd,BankAccount,RemoveAccountResponse

router = APIRouter(prefix="/bankAccountManagement", tags=["bankAccountManagement"])

@router.get("/", response_model=list[BankAccount])
async def get(user_id: int):
    return await getBankAccountDetails(user_id)

@router.post("/removeBankAccount", response_model=RemoveAccountResponse)
async def removeAccount(user_id: int, request: AccountRemove):  
    return await removeBankAccount(user_id, request)

@router.post("/addBankAccount")
async def addAccount(user_id: int, request: AccountAdd):
    return await addBankAccount(user_id, request)