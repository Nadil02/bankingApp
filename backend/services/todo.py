
from database import collection_Todo_list
from schemas.todo import TaskSchema
from fastapi import HTTPException
from datetime import datetime
from typing import Optional


async def mark_task_completed(user_id: int, todo_id: int):
    task = await collection_Todo_list.find_one({"user_id": user_id, "todo_id": todo_id})
    if not task:
        return {"message": "Task not found."}
    if task.get("status") == "Completed":
        return {"message": "Task is already completed."}
    result = await collection_Todo_list.update_one(
        {"user_id": user_id, "todo_id": todo_id},
        {"$set": {"status": "Completed"}}
    )
    if result.modified_count > 0:
        return {"message": "Task marked as completed."}
    else:
        return {"message": "Task update failed."}
    


async def check_task_existence(user_id: int, todo_id: int):
    task = await collection_Todo_list.find_one({"user_id": user_id, "todo_id": todo_id})
    if not task:
        return {"message": "Task not found."}
    return {"message": "Confirmation required", "description": f"Are you sure you want to remove the task: '{task['description']}'?"}



async def remove_task(user_id: int, todo_id: int, confirm: bool):
    if not confirm:
        return {"message": "Confirmed", "description": "Task not removed."}
    result = await collection_Todo_list.delete_one({"user_id": user_id, "todo_id": todo_id})
    if result.deleted_count == 0:
        return {"message": "Task not found."}
    return {"message": "success", "description": "Todo item removed successfully"}



async def get_task_details(user_id: int, todo_id: int):
    """Fetch task details from MongoDB"""
    task = await collection_Todo_list.find_one({"user_id": user_id, "todo_id": todo_id}, {"_id": 0})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if isinstance(task.get("date"), datetime):
        task["date"] = task["date"].strftime("%Y-%m-%d")
    if isinstance(task.get("time"), datetime):
        task["time"] = task["time"].strftime("%H:%M:%S")
    return TaskSchema(**task)




async def edit_task_details(user_id: int, todo_id: int, description: Optional[str] = None, date: Optional[datetime] = None, time: Optional[datetime] = None, repeat_frequency: Optional[str] = None):
    existing_task = await collection_Todo_list.find_one({"user_id": user_id, "todo_id": todo_id})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = {}
    if description is not None:
        update_data["description"] = description
    if date is not None:
        update_data["date"] = date.isoformat()  
    if time is not None:
        time_obj = time.replace(year=1900, month=1, day=1)  
        update_data["time"] = time_obj.isoformat()  
    if repeat_frequency is not None:
        update_data["repeat_frequency"] = repeat_frequency
    if not update_data:
        return {"message": "No changes were made"}
    await collection_Todo_list.update_one(
        {"user_id": user_id, "todo_id": todo_id},
        {"$set": update_data}
    )
    return {"message": "Task updated successfully"}