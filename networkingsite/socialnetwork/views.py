from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from .models import User
from .serializers import SignUpSerializer, LoginSerializer
from rest_framework.response import Response


# Create your views here.

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # sign-up is an open API, it isn't having any authentication 
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer
    lookup_field = 'uuid'
    
class LoginViewSet(APIView):
    # login is an open API, it isn't having any authentication 
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            return Response(serializer.create(serializer.validated_data), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)