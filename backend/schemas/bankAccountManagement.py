from pydantic import BaseModel,Field
from typing import Optional, List, Dict
from datetime import datetime

class AccountRemove(BaseModel):
    account_number: int
    NIC: str
    passcode: str

class AccountAdd(BaseModel):
    bank_account : str
    bank_id : int
    account_number : int
    account_type : str | None = None
    credit_limit : int | None = None
    due_date : datetime | None = None
    balance : float | None = None
    NIC : str 

class BankAccount(BaseModel):
    bank_id: int
    account_number: int
    account_type: str
    balance: float
    logo: str

class BankAccountResponse(BaseModel):
    message: List[BankAccount]  # Response contains a list of bank accounts

class RemoveAccountResponse(BaseModel):
    message: str
    description: str | None = None