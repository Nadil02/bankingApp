from pydantic import BaseModel,Field
from typing import Optional, List, Dict
from datetime import datetime

class AccountRemove(BaseModel):
    account_number: int
    NIC: str
    passcode: str

class AccountAdd(BaseModel):
    bank_name : str
    account_number : int
    account_type : str 
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

class BankAccountAddResponse(BaseModel):
    otp_id: int
    status: str
    message: str | None = None

class OtpRequestAccountAdding(BaseModel):
    user_id: int
    otp_id: int
    otp: str
    bank_name : str
    account_number : int
    account_type : str 

class OtpResponseAccountAdding(BaseModel):
    status: str
    message: str

class OtpResponseAccountAddingResend(BaseModel):
    status: str
    message: str
    otp_id: int

class OtpRequestAccountAddingResend(BaseModel):
    user_id: int
    otp_id: int



class BankInfo(BaseModel):
    bank_id: int
    bank_name: str
    logo: str

class BankListResponse(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[List[BankInfo]] = None