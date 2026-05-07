from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    @property
    def role(self):
        return 'Admin' if self.is_superuser else 'Member'

    def __str__(self):
        return f"{self.username} ({self.role})"
