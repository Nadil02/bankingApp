from fastapi import APIRouter, Depends, HTTPException
from services.incomeExpensePrediction import get_account_details_prediction
from schemas.incomeExpenseprediction import AccountPredictionResponse

router = APIRouter(prefix="/income_expense-prediction", tags=["Income Expense Predictions"])


@router.get("/all_accounts")
async def get_all_account_details_prediction(user_id: int) -> dict:
    return await get_account_details_prediction(user_id)


@router.get("/account_prediction", response_model=AccountPredictionResponse)
async def get_account_predictions(user_id: int, account_id: int) -> AccountPredictionResponse:
    from services.incomeExpensePrediction import get_predictions_for_account
    return await get_predictions_for_account(user_id, account_id)