from fastapi import HTTPException
from database import collection_Todo_list



async def get_ongoing_todos(user_id: int):
    # Query to match the user and only todos where status is "OnGoing"
    # Projection returns only description, date, and time fields.
    todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "OnGoing"},
        {"_id": 0, "description": 1, "date": 1, "time": 1}
    ).to_list(length=100)
    
    if todos:
        return todos
    raise HTTPException(status_code=404, detail="No ongoing todos found for this user")