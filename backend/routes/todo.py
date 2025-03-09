from fastapi import APIRouter, HTTPException
from schemas.todo import MarkCompletedRequest, RemoveTaskRequest, ConfirmTaskDeletion, TaskSchema, ResponseMessage
from services.todo import mark_task_completed, remove_task, check_task_existence, get_task_details, edit_task_details



router = APIRouter(
    prefix="/todo",
    tags=["todo"]
)

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
    result = await remove_task(request.user_id, request.task_id, request.confirm)
    if result["message"] == "Task not found.":
        raise HTTPException(status_code=404, detail=result["message"])
    return {"message": "Todo item removed successfully", "description": result["description"]}


@router.get("/task/", response_model=TaskSchema)
async def fetch_task_details(user_id: int, todo_id: int):
    """Fetch task details by user_id and task_id"""
    return await get_task_details(user_id, todo_id)




@router.put("/tasks/", response_model=ResponseMessage)
async def edit_task_details_route(user_id: int, todo_id: int, task: TaskSchema):
    """Edit task details in MongoDB"""
    return await edit_task_details(user_id, todo_id, task.description, task.date, task.time, task.repeat_frequency)