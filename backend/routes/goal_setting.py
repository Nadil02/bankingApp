from fastapi import APIRouter, HTTPException
from typing import List
from schemas.goal_setting import Account, Goal,GoalLoadRequest,GoalEditRequestResponse, GoalEditResponse, GoalEditRequest, GoalRequest,GoalResponseSchema
from services.goal_setting import get_savings_accounts_without_goals, set_goal, load_goal_to_edit, edit_goal, remove_goal_account_service, get_all_already_setup_goals

router = APIRouter()

@router.get("/accounts_for_goal_accounts", response_model=List[Account])
async def fetch_savings_accounts_without_goals(user_id: int):
    accounts = await get_savings_accounts_without_goals(user_id)
    return accounts




@router.post("/set_goal")
async def set_user_goal(goal: Goal):
    try:
        response = await set_goal(goal)
        return response  
    except HTTPException as e:
        raise e  
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error setting goal.")
    


@router.post("/goal_edit_request", response_model=GoalEditRequestResponse)
async def load_goal_page(request: GoalLoadRequest):
    user_id = request.user_id
    goal_id = request.goal_id
    goal_data = await load_goal_to_edit(user_id, goal_id)
    return goal_data




@router.post("/edit_goal", response_model=GoalEditResponse)
async def edit_goal_form_submission(request: GoalEditRequest):
    # Call the service to update the goal
    goal_data = await edit_goal(
        user_id=request.user_id,
        goal_id=request.goal_id,
        goal_name=request.goal_name,
        goal_amount=request.goal_amount,
        due_date=request.due_date
    )
    return goal_data



@router.delete("/remove-goal-account")
async def remove_goal_account(request: GoalRequest):
    return await remove_goal_account_service(request)

#endpoint to get all already setup goals
@router.get("/get_all_already_setup_goals", response_model=List[GoalResponseSchema])
async def get_goals(user_id: int):
    goals = await get_all_already_setup_goals(user_id)
    if not goals:
        raise HTTPException(status_code=404, detail="No goals found for this user")
    return goals