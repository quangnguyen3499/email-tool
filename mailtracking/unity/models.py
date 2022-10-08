from django.db import models

class Contact(models.Model):
    class Status(models.TextChoices):
        SUBSCRIBE = "SUBSCRIBE", "Subscribe"
        UNSUBSCRIBE = "UNSUBSCRIBE", "Unsubscribe"

    email = models.EmailField(unique=True)
    status = models.CharField(
        max_length=255, choices=Status.choices, default=Status.SUBSCRIBE, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
