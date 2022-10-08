from .models import Contact
from django.db import transaction

@transaction.atomic
def create_contact(
    *,
    email: str,
) -> Contact:
    contact = Contact(
        email=email,
    )
    contact.save()
    return contact
