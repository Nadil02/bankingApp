from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

# Response_model_for_returning_only_description_and_dates
class TodoOngoing(BaseModel):
    description: str 
    amount: int
    repeat_frequency: Optional[str] = None
    date: datetime
    time: datetime