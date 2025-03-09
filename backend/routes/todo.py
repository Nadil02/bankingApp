from fastapi import APIRouter, HTTPException
from schemas.todo import TodoOngoing
from services.todo import get_ongoing_todos_for_user
from typing import List
from models import TodoList
from services.todo import add_new_todo
from fastapi import status


router = APIRouter()

# GET endpoint to retrieve all ongoing todos for a particular user.
@router.get("/todos/ongoing/{user_id}", response_model=List[TodoOngoing])
async def get_ongoing_todos(user_id: int):
    todos = await get_ongoing_todos_for_user(user_id)
    if todos:
        return todos
    raise HTTPException(status_code=404, detail="No ongoing todos found for this user")

#add_new_todo
@router.post("/todos/", response_model=TodoList, status_code=status.HTTP_201_CREATED)
async def add_todo_item(todo: TodoList):
    created = await add_new_todo(todo)
    if created:
        return created
    raise HTTPException(status_code=400, detail="Failed to create todo item")