                                                                                                                                                                      
from typing import List
from datetime import datetime
from schemas.goal_setting import Account, Goal
from database import collection_goal, collection_account


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





async def set_goal(goal_data: Goal) -> str:
    try:
        account = await collection_account.find_one({"account_id": goal_data.account_id, "user_id": goal_data.user_id})
        if not account:
            raise ValueError("Account not found.")

        goal_data.start_date = datetime.now().strftime("%Y-%m-%d")

        goal_dict = goal_data.dict()
        result = await collection_goal.insert_one(goal_dict)

        await collection_account.update_one(
            {"account_id": goal_data.account_id, "user_id": goal_data.user_id},
            {"$push": {"associated_goals": result.inserted_id}}  
        )

        return "Goal set successfully."  
    
    except Exception as e:
        print(f"Error setting goal: {e}")
        return "Error setting goal."