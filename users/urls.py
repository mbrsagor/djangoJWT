from django.urls import path
from .views import profile, login_view

urlpatterns = [
    path('login', login_view, name="login"),
    path('profile', profile, name="profile"),
]
