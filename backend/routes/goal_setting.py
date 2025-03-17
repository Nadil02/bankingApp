from fastapi import APIRouter, HTTPException
from typing import List
from schemas.goal_setting import Account, Goal
from services.goal_setting import get_savings_accounts_without_goals, set_goal

router = APIRouter()

@router.get("/accounts_for_goal_accounts", response_model=List[Account])
async def fetch_savings_accounts_without_goals(user_id: int):
    accounts = await get_savings_accounts_without_goals(user_id)
    return accounts



@router.post("/set_goal")
async def set_user_goal(goal: Goal):
    """
    Endpoint to set or update a user's goal for a specific savings account.
    """
    response = await set_goal(goal)
    if response == "Goal set successfully.":
        return {"message": "Goal set successfully."}
    else:
        raise HTTPException(status_code=400, detail="Error setting goal.")