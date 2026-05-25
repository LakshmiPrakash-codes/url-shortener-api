from pydantic import BaseModel
from typing import Optional

class URLCreate(BaseModel):
    original_url: str
    custom_code: Optional[str] = None