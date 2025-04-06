from fastapi import HTTPException
from database import collection_Todo_list
from models import TodoList
from typing import List
from database import collection_Todo_list
from schemas.todo import TaskSchema, TodoCreate, TodoResponse, TodoView, TodoListsResponse
from fastapi import HTTPException
from datetime import datetime, date, time
from typing import Optional
from pymongo import DESCENDING


async def get_todos_by_status(user_id: int) -> TodoListsResponse:
    ongoing_todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "ongoing"},
        {"_id": 0, "description": 1, "date": 1, "time": 1, "repeat_frequency": 1, "amount": 1}
    ).to_list(length=100)
    
    completed_todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "Completed"},
        {"_id": 0, "description": 1, "date": 1, "time": 1, "repeat_frequency": 1, "amount": 1}
    ).to_list(length=100)
    
    return TodoListsResponse(
        ongoing=[TodoView(**todo) for todo in ongoing_todos],
        completed=[TodoView(**todo) for todo in completed_todos]
    )
"""#get_ongoing_todos
async def get_ongoing_todos_for_user(user_id: int)-> List[TodoView]:
    #Retrieve todos for the given user where status is 'OnGoing'.Returns only description, date, and time fields.
    
    todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "ongoing"},
        {"_id": 0, "description": 1, "date": 1, "time": 1,"amount":1,"repeat_frequency":1}
    ).to_list(length=100)
    return [TodoView(**todo) for todo in todos]"""

"""#addd_new_todo
async def add_new_todo(todo: TodoList):
    # Convert the Pydantic model to a dictionary using the alias (i.e., use "_id" for the todo_id)
    todo_dict = todo.dict(by_alias=True)
    result = await collection_Todo_list.insert_one(todo_dict)
    # Optionally, you can return the inserted document (or just the inserted_id)
    created_todo = await collection_Todo_list.find_one({"_id": todo_dict["_id"]})
    return created_todo"""

"""from pymongo import DESCENDING

async def get_next_todo_id():
    last_todo = await collection_Todo_list.find_one({}, sort=[("todo_id", DESCENDING)])  
    return last_todo["todo_id"] + 1 if last_todo else 1  # Ensure "todo_id" is an integer

async def add_new_todo(todo: TodoList):
    todo_dict = todo.dict(by_alias=True)

    # Auto-increment todo_id and ensure it's not taken from the frontend
    todo_dict.pop("todo_id", None)  # Remove todo_id if provided
    todo_dict["todo_id"] = await get_next_todo_id()  # Generate new todo_id

    result = await collection_Todo_list.insert_one(todo_dict)
    created_todo = await collection_Todo_list.find_one({"todo_id": todo_dict["todo_id"]})  
    
    return created_todo"""

async def get_next_todo_id() -> int:
    last_todo = await collection_Todo_list.find_one(sort=[("todo_id", -1)])
    return (last_todo["todo_id"] + 1) if last_todo else 1

async def add_todo(todo_data: TodoCreate) -> TodoResponse:
    todo_id = await get_next_todo_id()
    new_todo = {
        "todo_id": todo_id,
        "description": todo_data.description,
        "user_id": todo_data.user_id,
        "date": todo_data.date.isoformat(),  # Ensures proper date formatting
        "time": todo_data.time.isoformat(), 
        "repeat_frequency": todo_data.repeat_frequency,
        "amount": todo_data.amount,
        "status": "ongoing"
    }
    await collection_Todo_list.insert_one(new_todo)
    return TodoResponse(message="Item added successfully", todo_id=todo_id)


#update_todo_status(ongoing->completed)
"""async def update_todo_status(todo_id: int):
    
    Update the status of the todo with the given todo_id from "ongoing" to "Completed".
    Returns the updated document if the update was successful.
    
    update_result = await collection_Todo_list.update_one(
        {"todo_id": todo_id},
        {"$set": {"status": "Completed"}}
    )
    if update_result.modified_count == 1:
        updated_todo = await collection_Todo_list.find_one({"todo_id": todo_id})
        return updated_todo
    return None"""


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
    if isinstance(task.get("date"), date):
        task["date"] = task["date"].strftime("%Y-%m-%d")
    if isinstance(task.get("time"), time):
        task["time"] = task["time"].strftime("%H:%M:%S")
    return TaskSchema(**task)




async def edit_task_details(user_id: int, todo_id: int, description: Optional[str] = None, date: Optional[datetime] = None, time: Optional[datetime] = None, repeat_frequency: Optional[str] = None,amount: Optional[int] = None):
    existing_task = await collection_Todo_list.find_one({"user_id": user_id, "todo_id": todo_id})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = {}
    if description is not None:
        update_data["description"] = description
    if date is not None:
        update_data["date"] = date.isoformat()  
    if time is not None: 
        update_data["time"] = time.isoformat()  
    if repeat_frequency is not None:
        update_data["repeat_frequency"] = repeat_frequency
    if amount is not None:
        update_data["amount"] = amount
    """if not update_data:
        return {"message": "No changes were made"}"""
    await collection_Todo_list.update_one(
        {"user_id": user_id, "todo_id": todo_id},
        {"$set": update_data}
    )
    return {"message": "Task updated successfully"}
