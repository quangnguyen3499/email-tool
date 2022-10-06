from .models import Contact
from django.db.models.query import QuerySet

def email_list() -> QuerySet[Contact]:
    emails = (
        Contact.objects.order_by("created_at").reverse()
    )
    return emails

def get_contact_by_email(*, email: str) -> Contact:
    return Contact.objects.filter(email=email).first()
