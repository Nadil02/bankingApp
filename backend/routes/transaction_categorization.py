from fastapi import APIRouter, Depends, HTTPException
from services.transaction_categorization import get_account_details

router = APIRouter(prefix="/transaction_categorization", tags=["Transaction Categorization"])

@router.get("/all_accounts")
async def get_all_account_details(user_id: int) -> dict:
    return await get_account_details(user_id)