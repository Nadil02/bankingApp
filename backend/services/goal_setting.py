from fastapi import HTTPException                                                                                                                                                                  
from typing import List, Dict
from datetime import datetime
from schemas.goal_setting import Account, Goal, GoalEditRequestResponse, GoalEditResponse, GoalRequest
from database import collection_goal, collection_account
from bson import ObjectId


async def get_savings_accounts_without_goals(user_id: int) -> List[Account]:
    savings_accounts_cursor = collection_account.find({"user_id": user_id, "account_type": "savings"})
    goal_accounts_cursor = collection_goal.find({"user_id": user_id})
    goal_account_ids = {goal['account_id'] async for goal in goal_accounts_cursor}
    result = []
    async for account in savings_accounts_cursor:
        if account['account_id'] not in goal_account_ids:
            result.append(Account(
                account_number=str(account['account_number']),
                balance=account['balance'],
                bank_account=account['bank_account']
            ))
    
    return result 





async def set_goal(goal_data: Goal) -> Dict[str, str]:
    try:
        account = await collection_account.find_one(
            {"account_id": goal_data.account_id, "user_id": goal_data.user_id}
        )
        if not account:
            raise HTTPException(status_code=404, detail="Account not found.")
        goal_dict = goal_data.dict()  
        goal_dict["start_date"] = datetime.now().strftime("%Y-%m-%d") 
        await collection_goal.insert_one(goal_dict)
        return {"message": "Goal set successfully.", "account_id": goal_data.account_id}
    except HTTPException as http_exc:
        raise http_exc  
    except Exception as e:
        print(f"Error setting goal: {e}")
        raise HTTPException(status_code=400, detail="Error setting goal.")
    




async def load_goal_to_edit(user_id: int, goal_id: int) -> GoalEditRequestResponse:
    try:
        goal = await collection_goal.find_one({"user_id": user_id, "goal_id": goal_id})
        if not goal:
            raise HTTPException(status_code=404, detail="Goal not found.")
        return GoalEditRequestResponse(
            goal_name=goal.get("goal_name"),
            goal_amount=goal.get("goal_amount"),
            due_date=goal.get("due_date")
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error loading goal: {str(e)}")
    



async def edit_goal(user_id: str, goal_id: int, goal_name: str, goal_amount: float, due_date: str) -> GoalEditResponse:
    goal = await collection_goal.find_one({"user_id": user_id, "goal_id": goal_id})
    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found.")
    update_result = await collection_goal.update_one(
        {"user_id": user_id, "goal_id": goal_id},
        {"$set": {
            "goal_name": goal_name,
            "goal_amount": goal_amount,
            "due_date": due_date  
        }}
    )
    if update_result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No changes made to the goal.")
    goal_account_id = goal.get("goal_id")
    if goal_account_id is None or goal_account_id == "":
        goal_account_id = None  
    return GoalEditResponse(
        account_id=goal_account_id,
        status="success"
    )




async def remove_goal_account_service(data: GoalRequest) -> Dict[str, str]:
    query = {"user_id": data.user_id, "goal_id": data.goal_id, "account_id": data.account_id}
    result = await collection_goal.delete_one(query)  
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Goal account not found")
    
    return {"message": "Goal account removed successfully"}