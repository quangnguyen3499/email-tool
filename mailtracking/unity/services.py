from django.db import transaction
from .models import Contact

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
