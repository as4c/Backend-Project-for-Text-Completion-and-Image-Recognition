from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserRegistrationSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email','password')
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# class LoginSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('username','password')

