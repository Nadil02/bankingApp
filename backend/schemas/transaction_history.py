from pydantic import BaseModel
from typing import Optional
from datetime import date

class dashboard_request(BaseModel):
    account_id: int

class Dashboard_response(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: int

class Select_one_account_response(BaseModel):
    max_value : Optional[float] = None