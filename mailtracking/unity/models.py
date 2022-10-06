from django.db import models
from django.utils import timezone
from django.db.models import Count, Q

class Contact(models.Model):
    class Status(models.TextChoices):
        SUBSCRIBE = "SUBSCRIBE", "Subscribe"
        UNSUBSCRIBE = "UNSUBSCRIBE", "Unsubscribe"

    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.SUBSCRIBE, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def new_this_month(self):
        emails = Contact.objects.filter(created_at__month=timezone.now().month).count()
        return emails

    def ubsubscribed(self):
        emails = Contact.objects.filter(status=self.Status.UNSUBSCRIBE).count()
        return emails
