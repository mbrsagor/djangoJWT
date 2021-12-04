from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, MyTokenObtainPairView, CreateUserView, NoteListCreateView

router = DefaultRouter()
router.register('contact', ContactViewSet)

urlpatterns = [
    path('note/', NoteListCreateView.as_view(), name="note_endpoint"),
    path('auth/registration/', CreateUserView.as_view(), name="registration"),
    path('auth/login/', MyTokenObtainPairView.as_view(), name="login"),
] + router.urls
