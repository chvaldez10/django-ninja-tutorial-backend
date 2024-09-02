from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class WaitlistEntryCreateSchema(Schema):
    email: EmailStr
    
class WaitlistEntryDetailSchema(Schema):
    email: EmailStr
    timestamp: datetime