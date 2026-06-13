from pydantic import BaseModel, Field
from typing import List

class CustomerFeatures(BaseModel):
    recency: float = Field(..., ge=0)
    frequency: float = Field(..., ge=0)
    monetary: float = Field(..., ge=0)
    support_tickets: int = Field(..., ge=0)
    event_count: int = Field(..., ge=0)

class BatchRequest(BaseModel):
    customers: List[CustomerFeatures]
