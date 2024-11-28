from ninja import Schema
from datetime import datetime
from typing import List, Any
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    email: EmailStr
    
class WaitlistEntryListSchema(Schema):
    id: int
    email: EmailStr
    
class WaitlistEntryDetailSchema(Schema):
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
    
class ErrorWaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: List[Any]
    # non_field_errors: List[dict] = []
