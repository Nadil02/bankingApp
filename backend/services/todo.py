from fastapi import HTTPException
from database import collection_Todo_list




async def get_ongoing_todos_for_user(user_id: int):
    
    #Retrieve todos for the given user where status is 'OnGoing'.Returns only description, date, and time fields.
    
    todos = await collection_Todo_list.find(
        {"user_id": user_id, "status": "OnGoing"},
        {"_id": 0, "description": 1, "date": 1, "time": 1,"amount":1,"repeat_frequency":1}
    ).to_list(length=100)
    return todos