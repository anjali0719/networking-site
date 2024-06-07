from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from .models import User, FriendRequest
from .serializers import SignUpSerializer, LoginSerializer, UserSerializer, FriendRequestSerializer
from .constants import RequestStatusTypeChoices
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import action

# Create your views here.

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
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
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uuid'
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        queryset = User.objects.filter(is_active=True).order_by('-created_at')
        search = self.request.query_params.get('search', None)
        
        if search and search != '':
            queryset = User.objects.filter(Q(email__iexact=search) | Q(first_name__icontains=search))
            # q_filt = Q()
            # q_filt |= Q(email__iexact=search)
            # q_filt |= Q(first_name__icontains=search)
            # queryset = queryset.filter(q_filt)
           
        return queryset
        
    def get_serializer_context(self):
        data = super(UserViewSet, self).get_serializer_context()
        return data

    
class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all() 
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'uuid'
    
    
    def get_queryset(self):
        logged_in_user = self.request.user
        queryset = FriendRequest.objects.filter(from_user=logged_in_user).order_by('-created_at')
        return queryset
    
    def get_serializer_context(self):
        data = super(FriendRequestViewSet, self).get_serializer_context()
        return data
    
    """
        use this API to GET the list of Pending / Received Friend Requests of the current user
    """
    @action(
        detail=False,
        url_path='received-list',
        methods=['GET'],
        permission_classes=[permissions.IsAuthenticated],
    )
    def get_received_list(slef, request):
        logged_in_user = request.user
        queryset = FriendRequest.objects.filter(from_user=logged_in_user, status=RequestStatusTypeChoices.PENDING)
        
        results = FriendRequestSerializer(queryset, many=True)
        return Response(results.data)
    
    
    """
        use this API to GET the Friend's list(Accepted Requests) of the current user
    """
    @action(
        detail=False,
        url_path='friends-list',
        methods=['GET'],
        permission_classes=[permissions.IsAuthenticated],
    )
    
    def get_friends_list(self, request):
        logged_in_user = request.user
        queryset = FriendRequest.objects.filter(from_user=logged_in_user, status=RequestStatusTypeChoices.ACCEPTED)
        
        results = FriendRequestSerializer(queryset, many=True)
        return Response(results.data)

