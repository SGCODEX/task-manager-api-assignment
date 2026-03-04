from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    priority: str
    status: Optional[str] = "pending"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    external_reference_id: Optional[str] = None