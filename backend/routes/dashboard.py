from fastapi import APIRouter
from services.dashboard import get_user_name, load_full_details,load_specific_account,get_credit_summary
from schemas.dashboard import ResponseSchema

router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@router.get("/")
async def All_Account_DashBoard(user_id:int):
    # get user all bank accounts
    return await load_full_details(user_id)

@router.get("/all_account_time_period")
async def All_Account_DashBoard_With_Date(user_id:int,startdate:str,enddate:str ):
    return await load_full_details(user_id,startdate,enddate)

@router.get("/select_account")
async def savings_account(account_id: int, user_id:int):
    return await load_specific_account(account_id,user_id)

@router.get("/select_account_time_period")
async def saving_account_with_date(account_id:int,startdate:str,enddate:str):
    return await load_specific_account(account_id, start_date=startdate,end_date=enddate)

@router.get("/credit_card")
async def credit_card(account_id:int):
    return await get_credit_summary(account_id)

@router.get("/credit_card_time_period")
async def credit_card_with_date(account_id:int, time_period:int):
    return await get_credit_summary(account_id,time_period)

@router.get("/user_name")
async def user_name(user_id:int):
    return await get_user_name(user_id=user_id) #will return a string with the user name