from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Contact, Note

admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.register(Note)
