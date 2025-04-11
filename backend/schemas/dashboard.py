from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List
from typing import Optional
from typing import List,Dict, Any

class SelectAccountRequest(BaseModel):
    user_id: int
    account_id: int


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
    predicted_balance: float = 0.0 




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
    surplus_accounts: List[Dict[str, Any]] 


### Adding new pydantic models ###

class Account(BaseModel):
    _id: str
    bank_account: str
    account_id: int
    account_number: int
    account_type: str
    balance: float
    bank_logo: str

class Summary(BaseModel):
    total_income: float
    total_expenses: float
    total_savings: float

class CategorySpending(BaseModel):
    category_name: str
    total_spent: float
    category_precentage: float

class Transaction(BaseModel):
    date: datetime
    payment: float
    balance: float

class Prediction(BaseModel):
    date: date
    predicted_income: float
    predicted_expenses: float
    predicted_balance: float

class MostSpending(BaseModel):
    most_spending_category: str
    most_spending_amount: float

class Date(BaseModel):
    start_date: datetime
    end_date: datetime

class ResponseSchema(BaseModel):
    user_name: str
    accounts_list: List[Account]
    total_savings_accounts_balance: float
    financial_summary: Summary
    category_spending: List[CategorySpending]
    past_100_days_transactions: Dict[str, List[Dict[str, Any]]]
    upcoming_7_days_predictions: Dict[str, List[Dict[str, Any]]]
    most_spending: MostSpending
    date: Date

class CreditCardResponse(BaseModel):
    credit_limit : float
    total_expenses : float
    remaining_balance : float

class ResponseSchemaUsernameProfilePic(BaseModel):
    username: str
    user_image: str