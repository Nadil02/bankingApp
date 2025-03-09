from fastapi import APIRouter, Depends, HTTPException
from services.SerbankAccountManagement import getBankAccountDetails, removeBankAccount, addBankAccount
from models import AccountRemove, AccountAdd

router = APIRouter(prefix="/bankAccountManagement", tags=["bankAccountManagement"])

@router.get("/")
async def get(user_id: int):
    return await getBankAccountDetails(user_id)

@router.post("/removeBankAccount")
async def removeAccount(user_id: int, request: AccountRemove):  
    return await removeBankAccount(user_id, request)

@router.post("/addBankAccount")
async def addAccount(user_id: int, request: AccountAdd):
    return await addBankAccount(user_id, request)