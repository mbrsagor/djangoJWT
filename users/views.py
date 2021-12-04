from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import views, status, response
from rest_framework.generics import CreateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from .models import Contact, Note
from users import serializers
from .services import note_validate_service


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = (IsAuthenticated,)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [AllowAny, ]
    serializer_class = serializers.UserRegistrationSerializer


class NoteListCreateView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        note = Note.objects.all()
        serializer = serializers.NoteSerializer(note, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        validate_node_error = note_validate_service(request.data)
        if validate_node_error is not None:
            return response.Response(validate_node_error, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors)
