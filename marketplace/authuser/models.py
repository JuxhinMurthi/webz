from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Extend User Model to include address."""

    address = models.CharField(max_length=255, null=True, blank=True)

    @property
    def full_name(self):
        return self.get_full_name()
