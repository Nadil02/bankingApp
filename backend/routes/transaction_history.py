from fastapi import APIRouter
from schemas.transaction_history import dashboard_request
from services.transaction_history import load_all_accounts, select_one_account

router = APIRouter(prefix="/transaction_history", tags=["Transaction History"])

#load account list in transaction history page
@router.get("/")
async def load_transaction_history(account_id: int) -> dict:
    return await load_all_accounts(account_id)

#when user select account load it's details
@router.get("/select_account")
async def select_account(accont_id: int, user_id: int):
    return await select_one_account(user_id, accont_id)

#when user select 