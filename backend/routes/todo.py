from fastapi import APIRouter, HTTPException
from services.todo import get_todos_by_status, add_todo
from typing import List
"""from models import TodoList
from fastapi import status"""
from schemas.todo import MarkCompletedRequest, RemoveTaskRequest, ConfirmTaskDeletion, TaskSchema, ResponseMessage, TodoCreate, TodoResponse, TodoListsResponse
from services.todo import mark_task_completed, remove_task, check_task_existence, get_task_details, edit_task_details


router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)

# GET endpoint to retrieve all ongoing todos for a particular user.
@router.get("/TodoView", response_model=TodoListsResponse)
async def view_todos(user_id: int):
    todos = await get_todos_by_status(user_id)
    if todos:
        return todos
    raise HTTPException(status_code=404, detail="No ongoing todos found for this user")

#add_new_todo
"""@router.post("/add_todo/", response_model=List[TodoAdd], status_code=status.HTTP_201_CREATED)
async def add_todo_item(todo: TodoList):
    created = await add_new_todo(todo)
    if created:
        return created
    raise HTTPException(status_code=400, detail="Failed to create todo item")"""


@router.post("/add_todos", response_model=TodoResponse)
async def create_todo(todo: TodoCreate):
    return await add_todo(todo)


@router.post("/mark-completed/")
async def mark_as_completed(request: MarkCompletedRequest):
    result = await mark_task_completed(request.user_id, request.todo_id)
    if result["message"] == "Task not found.":
        raise HTTPException(status_code=404, detail=result["message"])
    if result["message"] == "Task is already completed.":
        raise HTTPException(status_code=400, detail=result["message"])
    return {"message": result["message"]}


@router.post("/remove/check/")
async def check_todo_item(request: RemoveTaskRequest):
    result = await check_task_existence(request.user_id, request.todo_id)
    if result["message"] == "Task not found.":
        raise HTTPException(status_code=404, detail=result["message"])
    return result


@router.delete("/remove/confirm/")
async def remove_todo_item(request: ConfirmTaskDeletion):
    result = await remove_task(request.user_id, request.todo_id, request.confirm)
    if result["message"] == "Task not found.":
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": result["message"], "description": result["description"]}


@router.get("/task/", response_model=TaskSchema)
async def fetch_task_details(user_id: int, todo_id: int):
    return await get_task_details(user_id, todo_id)


@router.post("/tasks/", response_model=ResponseMessage)
async def edit_task_details_route(user_id: int, todo_id: int, task: TaskSchema):
    return await edit_task_details(user_id, todo_id, task.description, task.date, task.time, task.repeat_frequency)
