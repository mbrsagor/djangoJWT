from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.contact_name[:20]
