from rest_framework import serializers
from . import models
import re
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
    

class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["firstName", "lastName", "address", "email", "password"]
        
        
    def validate_password(self, value):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter, "
                "one uppercase letter, one number, and one special character, "
                "and must be at least 8 characters long."
            )
        print(True)
        return value

    
    def validate_firstName(self, value):
        if len(value) < 1:
            raise serializers.ValidationError(
                "There must be firstname."
            )
        print(True)
        return value
    
    def validate_lastName(self, value):
        if len(value) < 1:
            raise serializers.ValidationError(
                "There must be lastname"
            )
        print(True)
        return value
    
    def validate_address(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Address must contain 5 characters."
            )
        print(True)
        return value
    
    #For the password hashing
    def create(self, validated_data):
        # generate the hash of the password
        validated_data["password"] = make_password(
            validated_data["password"]
        )
        print(True)
        return models.User.objects.create(
            **validated_data
        )

class LoginModelSerializer(serializers.Serializer):
    #Since I mentioned email to be unique so no need
    
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        email = data["email"]
        password = data["password"]
        
        
        # Search for such result
        user = models.User.objects.filter(email=email).first()
        print("Type of user: ", type(user))
        
        # after getting the user now just compare the password 
        if user is None:
            raise serializers.ValidationError(
                "Invalid email."
            )
            
        # Now check for the password
        if not check_password(password, user.password):
            raise serializers.ValidationError(
                "Invaid password"
            )
        
        # Now generate the jwt based on the user's data
        refresh = RefreshToken.for_user(user=user)
        
        
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }

        
        