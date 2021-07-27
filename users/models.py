from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self): return self.username


class DomainEntity(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(DomainEntity):
    contact_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.contact_name[:20]


class Note(DomainEntity):
    user = models.ForeignKey(User, related_name='note_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(default=None)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:30]
