from pydantic import BaseModel

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