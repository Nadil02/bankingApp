from fastapi import APIRouter, Depends, HTTPException
from services.incomeExpensePrediction import get_account_details_prediction, get_account_balance
from schemas.incomeExpenseprediction import AccountPredictionResponse

router = APIRouter(prefix="/income_expense-prediction", tags=["Income Expense Predictions"])


@router.get("/all_accounts")
async def get_all_account_details_prediction(user_id: int) -> dict:
    return await get_account_details_prediction(user_id)


@router.get("/account_prediction", response_model=AccountPredictionResponse)
async def get_account_predictions(user_id: int, account_id: int) -> AccountPredictionResponse:
    from services.incomeExpensePrediction import get_predictions_for_account
    return await get_predictions_for_account(user_id, account_id)

#######################################################################

# get predicted account balance for all accounts 
@router.get("/all_account_balance")
async def get_predicted_account_balance(user_id: int):
    return await get_account_balance(user_id)

# get predicted account balance for specific account
@router.get("/specific_account_balance", response_model=AccountPredictionResponse)
async def get_account_balance_by_id(user_id: int, account_id: int) -> AccountPredictionResponse:
    from services.incomeExpensePrediction import get_account_balance
    return await get_account_balance(user_id, account_id)