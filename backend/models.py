from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from uuid import uuid4

 
class user(BaseModel):
    first_name: str
    last_name: str
    nic: str
    phone_number: str
    passcode: str
    user_id: int 
    notification_status: bool


class account(BaseModel):
    bank_id: str
    account_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    user_id: int
    account_number: str
    account_type: str
    credit_limit: float
    due_date: datetime
    balance: float


class bank(BaseModel):
    bank_name: str
    logo: str
    bank_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")


class OTP(BaseModel):
    otp: str
    user_id: int
    otp_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    expiry_time: datetime
    verification_count: int


class TodoList(BaseModel):
    description: str
    todo_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    user_id: int
    date: datetime
    time: datetime
    repeat_frequency: Optional[str] = None


class transaction(BaseModel):
    transaction_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    category_id: str
    account_id: str
    date: datetime
    description: str
    balance: float
    payment: float
    receipt: float


class PredictedBalance(BaseModel):
    account_id: str
    prediction_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    date: datetime
    description: str
    explanation: str
    balance: float


class PredictedExpense(BaseModel):
    account_id: str
    prediction_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    date: datetime
    description: str
    explanation: str
    amount: float



class PredictedIncome(BaseModel):
    account_id: str
    prediction_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    date: datetime
    description: str
    explanation: str
    amount: float




class Notification(BaseModel):
    user_id: int
    notification_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    description: str
    date: datetime
    time: datetime
    notification_type: str 
    status: str  



class TransactionCategory(BaseModel):
    category_name: str
    category_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")



class Goal(BaseModel):
    account_id: str
    goal_id: str =Field(default_factory=lambda: str(uuid4()), alias="_id")
    goal_name: str
    goal_amount: float
    start_date: datetime
    due_date: datetime


class ChatBot(BaseModel):
    user_id: int
    chat_summary: str

class UserDummy(BaseModel):
    user_id: str
    amount: Optional[float] = None
    accountNumber: Optional[str] = None
    name: Optional[str] = None

