from fastapi import HTTPException
from database import collection_Todo_list
from models import TodoList
from typing import List



#get_ongoing_todos
async def get_ongoing_todos_for_user(user_id: int):
    
    #Retrieve todos for the given user where status is 'OnGoing'.Returns only description, date, and time fields.
    
    todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "OnGoing"},
        {"_id": 0, "description": 1, "date": 1, "time": 1,"amount":1,"repeat_frequency":1}
    ).to_list(length=100)
    return todos

#addd_new_todo
async def add_new_todo(todo: TodoList):
    # Convert the Pydantic model to a dictionary using the alias (i.e., use "_id" for the todo_id)
    todo_dict = todo.dict(by_alias=True)
    result = await collection_Todo_list.insert_one(todo_dict)
    # Optionally, you can return the inserted document (or just the inserted_id)
    created_todo = await collection_Todo_list.find_one({"_id": todo_dict["_id"]})
    return created_todo

#update_todo_status(ongoing->completed)
async def update_todo_status(todo_id: int):
    """
    Update the status of the todo with the given todo_id from "ongoing" to "Completed".
    Returns the updated document if the update was successful.
    """
    update_result = await collection_Todo_list.update_one(
        {"todo_id": todo_id},
        {"$set": {"status": "Completed"}}
    )
    if update_result.modified_count == 1:
        updated_todo = await collection_Todo_list.find_one({"todo_id": todo_id})
        return updated_todo
    return None
