from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import login_view, ContactViewSet

router = DefaultRouter()
router.register('contact', ContactViewSet)

urlpatterns = [
    path('auth/login/', login_view, name="login"),
] + router.urls
