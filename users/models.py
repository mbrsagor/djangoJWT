from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self): return self.username


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contact_name[:20]
