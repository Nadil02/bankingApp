from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class dashboard_request(BaseModel):
    account_id: int

class Dashboard_response(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: int
    image_url: Optional[str] = None

class Select_one_account_response(BaseModel):
    max_value : Optional[float] = None
    first_transaction_date: Optional[str] = None

class TimeFrame(BaseModel):
    period_id: int
    start_date: date
    end_date: date  
class TimeFrameResponse(BaseModel):
    available_past_time_frames: List[TimeFrame]
    current_time_frame: TimeFrame