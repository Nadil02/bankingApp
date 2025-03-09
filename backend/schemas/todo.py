from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class MarkCompletedRequest(BaseModel):
    user_id: int
    todo_id: int


class RemoveTaskRequest(BaseModel):
    user_id: int
    todo_id: int


class ConfirmTaskDeletion(BaseModel):
    user_id: int
    todo_id: int
    confirm: bool



class TaskSchema(BaseModel):
    description: str
    date: Optional[datetime] 
    time: Optional[datetime] 
    repeat_frequency: Optional[str] = None


    #class Config:
     #   orm_mode = True

class ResponseMessage(BaseModel):
    message: str
    