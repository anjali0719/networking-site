from rest_framework import serializers, status
from rest_framework.response import Response
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


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
        
