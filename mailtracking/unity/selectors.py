from .models import Contact
from django.utils import timezone
from datetime import datetime
from django.db.models.query import QuerySet


def email_list() -> QuerySet[Contact]:
    emails = Contact.objects.order_by("created_at").reverse()
    return emails


def get_contact_by_email(*, email: str) -> Contact:
    return Contact.objects.filter(email=email).first()


def new_email_current_month():
    emails = Contact.objects.filter(
        created_at__month=timezone.now().month,
        created_at__year=timezone.now().year,
    ).count()
    return emails


def unsubscribed_email():
    emails = Contact.objects.filter(status=Contact.Status.UNSUBSCRIBE).count()
    return emails


def get_email_statistic():
    new_email_this_month = new_email_current_month()
    count = Contact.objects.count()
    unsubscribed = unsubscribed_email()
    time = datetime.now().strftime("%B %Y")

    return {
        "new_email_this_month": new_email_this_month,
        "count": count,
        "unsubscribed": unsubscribed,
        "time": time,
    }
