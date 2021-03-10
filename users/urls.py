from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, MyTokenObtainPairView, CreateUserView

router = DefaultRouter()
router.register('contact', ContactViewSet)

urlpatterns = [
                  path('auth/registration/', CreateUserView.as_view(), name="registration"),
                  path('auth/login/', MyTokenObtainPairView.as_view(), name="login"),
              ] + router.urls
