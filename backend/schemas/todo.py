from pydantic import BaseModel, Field,validator 
from datetime import datetime, date, time
from typing import List, Optional

# Response_model_for_returning_only_description_and_dates
class TodoView(BaseModel):
    description: str
    date: Optional[str]
    time: Optional[str]
    repeat_frequency: Optional[str]
    amount: Optional[float]

class TodoListsResponse(BaseModel):
    ongoing: List[TodoView]
    completed: List[TodoView]


"""class TodoAdd(BaseModel):
    description:str
    user_id:str
    date:str
    time:str
    repeat_frequency: Optional[str] = None
    amount: int"""


class TodoCreate(BaseModel):
    description: str
    user_id: int
    date: Optional[str]  # Stores only the date part
    time: Optional[str]
    repeat_frequency: Optional[str] = None
    amount: Optional[float] = None
    
class TodoResponse(BaseModel):
    message: str
    todo_id: int


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
    date: Optional[str] 
    time: Optional[str] 
    repeat_frequency: Optional[str] = None
    amount:int


    #class Config:
     #   orm_mode = True

class ResponseMessage(BaseModel):
    message: str
    
