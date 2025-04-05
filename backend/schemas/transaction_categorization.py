from typing import Optional
from pydantic import BaseModel

class all_ac_details_response(BaseModel):
    account_id: int
    account_number: int
    account_type: str
    balance: int
    image_url: Optional[str] = None