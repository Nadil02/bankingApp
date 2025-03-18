from pydantic import BaseModel
from datetime import date
from typing import Optional
class Account(BaseModel):
    account_number: str
    balance: float
    bank_account: str

class Goal(BaseModel):
    account_id: int
    goal_name: str
    goal_amount: float
    due_date: str   
    user_id: int


class GoalLoadRequest(BaseModel):
    user_id: int
    goal_id: int


class GoalEditRequestResponse(BaseModel):
    goal_name: str
    goal_amount: float
    due_date: date



class GoalEditResponse(BaseModel):
    account_id: Optional[int]
    status: str



class GoalEditRequest(BaseModel):
    user_id: int
    goal_id: int
    goal_name: str
    goal_amount: float
    due_date: str



class GoalRequest(BaseModel):
    user_id: int
    goal_id: int
    account_id: int

#for retreiing goal(already setup goal)
class GoalResponseSchema(BaseModel):
    goal_id: int
    goal_name: str
    goal_amount: int
    due_date: str
    start_date: str
    account_id: int
    balance: float  # Latest balance from transactions