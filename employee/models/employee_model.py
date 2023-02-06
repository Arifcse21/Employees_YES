from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Employee(AbstractUser):
    uuid = models.UUIDField(uuid.uuid4(), editable=False, null=True, blank=True)
    pwd = models.CharField(max_length=255, null=True, blank=True)

