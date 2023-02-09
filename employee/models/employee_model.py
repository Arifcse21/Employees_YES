from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class Employee(AbstractUser):
    uuid = models.UUIDField(uuid.uuid4(), editable=False, null=True, blank=True)
    passwd = models.CharField(max_length=255, null=True, blank=True)    # Just for development purpose
    address = models.CharField(max_length=255, null=True, blank=True)
    contact_no = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username


