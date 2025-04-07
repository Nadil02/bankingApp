from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import date

class all_ac_details_response(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: int
    image_url: Optional[str] = None

class Transaction(BaseModel):
    transaction_id: int
    amount: float
    date: date
    description: Optional[str]


class CategoryDetails(BaseModel):
    category_name: str
    category_id: int
    transaction_count: int
    transactions: List[Transaction]

class category_details_response(BaseModel):
    income: Dict[int, CategoryDetails]  # Key is category_id
    expense: Dict[int, CategoryDetails]  # Key is category_id

class CategorizeTransactionConfirmationRequest(BaseModel):
    transaction_id: int
    previous_category_id: int
    new_category_id: int

class categorize_transaction_confirmation_response(BaseModel):
    message: str
    transaction_id: int
    previous_category_id: int
    new_category_id: int


class edit_category_name_request(BaseModel):
    category_id: int
    new_category_name: str

class edit_category_name_response(BaseModel):
    message: str
    category_id: int
    new_category_name: str

class remove_this_transaction_from_category_request(BaseModel):
    transaction_id: int
    category_id: int

class remove_this_transaction_from_category_response(BaseModel):
    message: str
    transaction_id: int
    category_id: int
