from rest_framework import serializers, status
from rest_framework.response import Response
from .models import User, FriendRequest
from .constants import RequestStatusTypeChoices
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import datetime, timedelta


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "password",
            "first_name",
        ]
    
    def create(self, validated_data):
        try:
            first_name = validated_data.get("email")
            first_name = first_name.split('@')[0]
            username = validated_data.get("email")
            instance = User.objects.create(first_name=first_name, username=username, **validated_data)
            return instance
        
        except Exception as error:
            print(f"An error occurred while Signing-Up the customer: {error}")
            return Response(
                {
                    'message': 'An error occurred while Signing-Up the customer',
                    'error': error
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

            
class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "password",
            "first_name",
        ]
    
    def validate(self, data):
        request = self.context.get('request')
        data = request.data
        email = data.get("email")
        password = data.get("password")
        
        if email and password:
            user = User.objects.filter(email=email, password=password).first()
            
            if user is None:
                return Response(
                    {'message': 'Wrong credentials provided'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                data['user'] = user
        else:
            raise serializers.ValidationError("Email & Password not provided")
            
        return data
        
    def create(self, validated_data):
        try:
            user = validated_data['user']
            refresh = RefreshToken.for_user(user)
            return {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            }
        
        except Exception as error:
            print(f"An error occurred while generating the token: {error}")
            return Response(
                {
                    'message': 'An error occurred while generating the token',
                    'error': error
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "password",
            "first_name"
        ]
        

class FriendRequestSerializer(serializers.ModelSerializer):
    to_user_uuid = serializers.UUIDField(source='to_user.uuid', default=None, write_only=True)
    from_user_uuid = serializers.UUIDField(source='from_user.uuid', required=False, write_only=True)
    class Meta:
        model = FriendRequest
        fields = [
            "uuid",
            "from_user",
            "from_user_uuid",
            "to_user",
            "to_user_uuid",
            "status"
        ]
        read_only_fields = ['from_user', 'to_user']
        
    def create(self, validated_data):
        try:
            to_user_uuid = validated_data.pop('to_user')['uuid']
            to_user = User.objects.filter(uuid=to_user_uuid).first()
            from_user = self.context.get('request').user
            time_limit = timezone.now() - timedelta(minutes=3)
            friend_request = None
            
            if from_user and to_user:
                if FriendRequest.objects.filter(to_user=to_user, from_user=from_user, created_at__gte=time_limit).count() > 3:
                    raise serializers.ValidationError("You cannot send more than 3 friend request within a minute")

                elif FriendRequest.objects.filter(to_user=to_user, from_user=from_user).exists():
                    raise serializers.ValidationError("You already have a friend request from this user")

                else:
                    friend_request = FriendRequest.objects.create(status=RequestStatusTypeChoices.PENDING, **validated_data)
            else:
                raise serializers.ValidationError("User to send request not provided") 
            
            return friend_request
            
        except Exception as error:
            print(f"Something went wrong while sending the friend request: {error}")
            return Response(
                {
                    'message': "Something went wrong while sending the friend request",
                    'error': error
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
