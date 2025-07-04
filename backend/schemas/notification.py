from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Notification(BaseModel):
    type: Optional[str]
    account_id: Optional[int]
    minus_balance: Optional[float]
    transaction_date: Optional[datetime]
    todo_amount: Optional[float]
    todo_date: Optional[datetime]
    user_id: int
    seen: Optional[bool] = False