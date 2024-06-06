from django.db import models
import uuid
from datetime import datetime

# Create your models here.

def generate_uuid():
    """
        Generates UUID Object combined with timestamp
    """
    return uuid.uuid3(uuid.uuid4(), str(datetime.timestamp(datetime.now())))

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=generate_uuid, editable=False, unique=True)
    
    class Meta:
        abstract = True
