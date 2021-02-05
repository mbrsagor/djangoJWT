from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import profile, login_view, ContactViewSet

router = DefaultRouter()
router.register('contact-list', ContactViewSet)

urlpatterns = [
    path('auth/login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
] + router.urls
