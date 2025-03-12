from fastapi import APIRouter
from services.dashboard_new import update_second_header,load_full_details,load_specific_account,get_credit_summary

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"]
)

@router.get("/")
async def displayDashBoard(user_id:int):
    # get user all bank accounts
    return await load_full_details(user_id)

@router.get("/all_account_time_period")
async def displayDashBoardWithDate(user_id:int,startdate:str,enddate:str ):
    return await load_full_details(user_id,startdate,enddate)

@router.get("/select_account")
async def savings_summary(account_id: str):
    return await load_specific_account(account_id)

@router.get("/select_account_time_period")
async def func(account_id:str,startdate:str,enddate:str):
    return await load_specific_account(account_id, startdate,enddate)

@router.get("/credit_card")
async def func(account_id:str):
    return await get_credit_summary(account_id)

@router.get("/credit_card_time_period")
async def func(account_id:str, time_period:int):
    return await get_credit_summary(account_id,time_period)
