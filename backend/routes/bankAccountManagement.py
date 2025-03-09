from fastapi import APIRouter
from services.SerbankAccountManagement import load_bank_accounts_details

router = APIRouter(prefix="/bankAccountManagement", tags=["bankAccountManagement"])

@router.get("/")
async def get_all_bank_accounts(user_id: int):
    return await load_bank_accounts_details(user_id)

@router.get("/remove_account")
def remove_bank_account():
    return {"message": "Remove bank account"}

@router.get("/add_account")
def add_bank_account():
    return {"message": "Add bank account"}