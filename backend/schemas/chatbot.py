from datetime import datetime
from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    user_id: str
    query: str

class ChatbotResponse(BaseModel):
    response: str

class GetTotalSpendingsArgs(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime

class GetTotalIncomeArgs(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime

class GetLastTransactionArgs(BaseModel):
    user_id: str

class GetMonthlySummaryArgs(BaseModel):
    user_id: str
    month: int

class GetAllTransactionsForDateArgs(BaseModel):
    user_id: str
    date: datetime

class GetNextMonthTotalIncomesArgs(BaseModel):
    user_id: str

class GetNextMonthTotalSpendingsArgs(BaseModel):
    user_id: str

class GetNextIncomeArgs(BaseModel):
    user_id: str

class GetNextSpendingArgs(BaseModel):
    user_id: str

class HandleIncompleteTimePeriodsArgs(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime

