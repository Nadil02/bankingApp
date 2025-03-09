from pydantic import BaseModel, Field,validator 
from datetime import datetime
from typing import List, Optional

# Response_model_for_returning_only_description_and_dates
class TodoOngoing(BaseModel):
    description: str 
    amount: int
    repeat_frequency: Optional[str] = None
    date: datetime
    time: datetime


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
    
