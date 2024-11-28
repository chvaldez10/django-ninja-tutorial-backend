from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from .schemas import WaitlistEntryListSchema, WaitlistEntryDetailSchema, ErrorWaitlistEntryCreateSchema, WaitlistEntryCreateSchema
from .models import WaitlistEntry
from .forms import WaitlistEntryCreateForm
import helpers
import json

router = Router()

# /api/waitlists/
@router.get("", response=List[WaitlistEntryListSchema])
def list_waitlist_entries(request):
    qs = WaitlistEntry.objects.all()
    return qs

@router.post("",
             response={201: WaitlistEntryDetailSchema, 400: ErrorWaitlistEntryCreateSchema}, auth=helpers.api_auth_user_or_annon)
def create_waitlist_entry(request, data:WaitlistEntryCreateSchema):
    form = WaitlistEntryCreateForm(data.dict())
    
    if not form.is_valid():
        form_errors = json.loads(form.errors.as_json())
        return 400, form_errors
    
    obj = form.save(commit=False)
    
    if request.user.is_authenticated:
        obj.user = request.user
    obj.save()
    
    return 201, obj

# /api/waitlists/{entry_id}/
@router.get("{entry_id}/", response=WaitlistEntryDetailSchema)
def get_waitlist_entry(request, entry_id:int):
    obj = get_object_or_404(WaitlistEntry, id=entry_id)
    return {
        "id": obj.id,
        "email": obj.email,
        "updated": obj.updated,
        "timestamp": obj.timestamp,
    }
    
