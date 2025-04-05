from fastapi import APIRouter, Depends, HTTPException
from services.transaction_categorization import get_account_details, get_category_details
from schemas.transaction_categorization import category_details_response

router = APIRouter(prefix="/transaction_categorization", tags=["Transaction Categorization"])

@router.get("/all_accounts")
async def get_all_account_details(user_id: int) -> dict:
    return await get_account_details(user_id)

@router.get("/get_category_details")
async def get_all_category_details(user_id: int,account_id:int) -> category_details_response:
    return await get_category_details(user_id,account_id)
    




