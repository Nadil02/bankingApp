from fastapi import APIRouter, Depends, HTTPException
from services.transaction_categorization import get_account_details, get_category_details, categorize_transaction_confirmation, edit_category_name, remove_this_transaction_from_category
from schemas.transaction_categorization import category_details_response,CategorizeTransactionConfirmationRequest,categorize_transaction_confirmation_response,all_ac_details_response,edit_category_name_response,edit_category_name_request,remove_this_transaction_from_category_request,remove_this_transaction_from_category_response

router = APIRouter(prefix="/transaction_categorization", tags=["Transaction Categorization"])

@router.get("/all_accounts")
async def get_all_account_details(user_id: int) -> dict:
    return await get_account_details(user_id)

@router.get("/get_category_details")
async def get_all_category_details(user_id: int,account_id:int) -> category_details_response:
    return await get_category_details(user_id,account_id)

@router.post("/categorize_transaction_confirmation")
async def categorize_transaction_confirmation_endpoint(request: CategorizeTransactionConfirmationRequest) -> categorize_transaction_confirmation_response:
    return await categorize_transaction_confirmation(request.transaction_id, request.previous_category_id, request.new_category_id)   

@router.post("/edit_category_name")
async def edit_category_name_endpoint(request: edit_category_name_request) -> edit_category_name_response:
    return await edit_category_name(request.category_id, request.new_category_name)

@router.post("/remove_this_transaction_from_category")
async def remove_this_transaction_from_category_endpoint(request: remove_this_transaction_from_category_request) -> remove_this_transaction_from_category_response:
    return await remove_this_transaction_from_category(request.transaction_id, request.category_id)