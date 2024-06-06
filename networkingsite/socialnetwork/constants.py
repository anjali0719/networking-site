from django.db import models

class RequestStatusTypeChoices(models.TextChoices):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    PENDING = "pending"
    
