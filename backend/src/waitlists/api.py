from typing import List
from ninja import Router
from .schemas import WaitlistEntryListSchema
from .models import WaitlistEntry

router = Router()

@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs