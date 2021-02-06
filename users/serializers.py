import datetime
from rest_framework import serializers
from .models import User, Contact

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.utils import datetime_to_epoch

SUPERUSER_LIFETIME = datetime.timedelta(minutes=30)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'is_active']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id', 'contact_name', 'contact_number'
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token['user_id'] = user.id
        token['name'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['is_active'] = user.is_active
        if user:
            token.payload['exp'] = datetime_to_epoch(token.current_time + SUPERUSER_LIFETIME)
            return token
