from pydantic import BaseModel
from datetime import datetime
from typing import List
from typing import Optional

class SelectAccountRequest(BaseModel):
    user_id: int
    account_id: str


class SpendingCategory(BaseModel):
    category_name: str
    total_spent: float

class PastTransaction(BaseModel):
    date: datetime
    payment: Optional[float] = None
    receipt: Optional[float] = None
    balance: float


class FutureTransaction(BaseModel):
    date: datetime
    predicted_income: float
    predicted_expenses: float
    predicted_balance: float


class NegativeBalance(BaseModel):
    date: datetime
    predicted_balance: float




class SelectedAccountResponse(BaseModel):
    total_income: float
    total_expenses: float
    total_savings: float
    start_date: datetime
    end_date: datetime
    top_categories: List[SpendingCategory]
    past_data: Optional[List[PastTransaction]] = None
    future_data: Optional[List[FutureTransaction]] = None
    most_spent_category_name: Optional[str] = "Unknown"
    most_spent_amount: Optional[float] = 0.0
    negative_balance_prediction: Optional[List[NegativeBalance]] = None


