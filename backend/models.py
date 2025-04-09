from pydantic import BaseModel,Field
from typing import Optional, List, Dict
from datetime import datetime
from uuid import uuid4
from typing import List, Dict, Any


 
class user(BaseModel):
    first_name: str
    last_name: str
    username: str
    NIC: str
    login_nic:str
    phone_number: str
    passcode: str
    user_id: int =Field(default_factory=lambda: int(uuid4()), alias="_id")
    notification_status: bool
    user_image: str


class account(BaseModel):
    bank_id: str
    account_id: int =Field(default_factory=lambda: int(uuid4()), alias="_id")
    user_id: int
    account_number: int
    account_type: str
    credit_limit: float
    due_date: Optional[datetime]=None
    balance: float


class bank(BaseModel):
    bank_name: str
    logo: str
    bank_id: int
    #rates as array of dictionaries
    rates: List[dict] = []  # Assuming you want to store multiple rates


class OTP(BaseModel):
    otp: str
    # user_id: int
    otp_id: int
    # expiry_time: datetime
    # verification_count: int


class TodoList(BaseModel):
    description: str
    todo_id: Optional[int] = None 
    user_id: int
    date: datetime
    time: datetime
    repeat_frequency: Optional[str] = None
    amount: Optional[float] = None
    status: str = Field(default="ongoing")


class transaction(BaseModel):
    transaction_id: int
    category_id: int
    account_id: int
    date: datetime
    description: str
    balance: float
    payment: float
    receipt: float


class PredictedBalance(BaseModel):
    account_id: int
    prediction_id: int
    date: datetime
    description: str
    explanation: str
    balance: float


class PredictedExpense(BaseModel):
    account_id: int
    prediction_id: int
    date: datetime
    description: str
    explanation: str
    amount: float



class PredictedIncome(BaseModel):
    account_id: int
    prediction_id: int
    date: datetime
    description: str
    explanation: str
    amount: float




class Notification(BaseModel):
    user_id: str
    notification_id: int
    description: str
    date: datetime
    time: datetime
    notification_type: str 
    status: str  



class TransactionCategory(BaseModel):
    category_name: str
    category_id: int



class Goal(BaseModel):
    account_id: int
    goal_id: int
    goal_name: str
    goal_amount: float
    start_date: datetime
    due_date: datetime


class ChatBot(BaseModel):
    user_id: int
    chat_summary: str
    tool_history: List[str] 


class credit_periods(BaseModel):
    acocunt_id: int
    period_id: int
    credit_limit: float
    total_expenses: float
    remaining_balance: float
    start_date: datetime
    end_date: datetime


class UserDummy(BaseModel):
    user_id: int
    amount: Optional[float] = None
    accountNumber: Optional[str] = None
    name: Optional[str] = None

