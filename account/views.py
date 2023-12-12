# myapp/views.py
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message':'Login Successfull.','token': token.key}, status=status.HTTP_200_OK)
        else:
            print("Authentication failed")
            return Response({'error': 'Invalid username or password. Please check your credentials and try again.'}, status=status.HTTP_401_UNAUTHORIZED)
