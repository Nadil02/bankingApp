from datetime import datetime
from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    user_id: int
    query: str

class ChatbotResponse(BaseModel):
    response: str

class GetTotalSpendingsArgs(BaseModel):
    user_id: int
    start_date: datetime
    end_date: datetime

class GetTotalIncomeArgs(BaseModel):
    user_id: int
    start_date: datetime
    end_date: datetime

class GetLastTransactionArgs(BaseModel):
    user_id: int

class GetMonthlySummaryArgs(BaseModel):
    user_id: int
    year: int
    month: int

class GetAllTransactionsForDateArgs(BaseModel):
    user_id: int
    date: datetime

class GetNextMonthTotalIncomesArgs(BaseModel):
    user_id: int

class GetNextMonthTotalSpendingsArgs(BaseModel):
    user_id: int

class GetNextIncomeArgs(BaseModel):
    user_id: int

class GetNextSpendingArgs(BaseModel):
    user_id: int