from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from .models import Contact
from .serializers import ContactSerializer, CustomTokenObtainPairSerializer, UserRegistrationSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [AllowAny, ]
    serializer_class = UserRegistrationSerializer
