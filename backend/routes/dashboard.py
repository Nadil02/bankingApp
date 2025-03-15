from fastapi import APIRouter
from services.dashboard import load_full_details,load_specific_account,get_credit_summary

router = APIRouter(prefix="/dashboard",tags=["dashboard"])

@router.get("/")
async def Display_DashBoard(user_id:int):
    # get user all bank accounts
    return await load_full_details(user_id)

@router.get("/all_account_time_period")
async def Display_Dash_Board_With_Date(user_id:int,startdate:str,enddate:str ):
    return await load_full_details(user_id,startdate,enddate)

@router.get("/select_account")
async def Summary_For_Specific_Account(user_id:int,account_id: str):
    return await load_specific_account(user_id,account_id)

@router.get("/select_account_time_period")
async def Summary_For_Specific_Account_With_Date(account_id:str,startdate:str,enddate:str):
    return await load_specific_account(account_id, startdate,enddate)

@router.get("/credit_card")
async def Credit_Card_Info(account_id:int):
    return await get_credit_summary(account_id)

@router.get("/credit_card_time_period")
async def Credit_Card_Info_With_Time_Period(account_id:str, time_period:int):
    return await get_credit_summary(account_id,time_period)