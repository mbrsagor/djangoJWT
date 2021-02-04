from django.urls import path
from .views import profile, login_view

urlpatterns = [
    path('auth/login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
]
