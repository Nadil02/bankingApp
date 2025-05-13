from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import date
from datetime import datetime

class all_ac_details_response_prediction(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: int
    image_url: Optional[str] = None



class PredictionItem(BaseModel):
    user_id: int
    account_id: int
    Date: datetime
    amount: float
    category_name: str
    explanation: str
    clasification_uncertainity: float
    regression_uncertainity: float
    transaction_type: str 

class AccountPredictionResponse(BaseModel):
    expenses: list[PredictionItem]
    income: list[PredictionItem]

class AllAccountBalanceResponse(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: float
    image_url: Optional[str] = None