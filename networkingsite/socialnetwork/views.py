from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from .models import User
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


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
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        queryset = User.objects.all().order_by('-created_at')
        search = self.request.query_params.get('search', None)
        
        if search and search != '':
            q_filt = Q()
            q_filt |= Q(email__iexact=search)
            q_filt |= Q(first_name__icontains=search)
            queryset = queryset.filter(q_filt)
           
        return queryset
        
    def get_serializer_context(self):
        data = super(UserViewSet, self).get_serializer_context()
        return data
    
