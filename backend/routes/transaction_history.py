from fastapi import APIRouter
from schemas.transaction_history import dashboard_request
from services.transaction_history import get_credit_card_timeframes, load_all_accounts, select_one_account, get_transactions_details, get_transactions_credit_card_details

router = APIRouter(prefix="/transaction_history", tags=["Transaction History"])

#load account list in transaction history page
@router.get("/")
async def load_transaction_history(account_id: int) -> dict:
    return await load_all_accounts(account_id)

#when user select account load it's details
@router.get("/select_account")
async def select_account(accont_id: int, user_id: int):
    return await select_one_account(user_id, accont_id)

#when user select date and range fro saving account
@router.get("/get_transactions")
async def get_transactions_history_within_date_and_time(account_id: int, start_date: str, end_date: str, range_start: float=None, range_end: float=None, value: float=None):
    return await get_transactions_details(account_id, start_date, end_date, range_start, range_end, value)

@router.get("/select_credit_card_account")
async def select_credit_card_account(account_id: int, user_id: int):
    return await get_credit_card_timeframes(user_id, account_id)

#when user select date and range for credit card
@router.get("/get_transactions_credit_card")
async def get_transactions_credit_card(user_id:int, account_id: int, time_period:int):
    return await get_transactions_credit_card_details(user_id, account_id, time_period)