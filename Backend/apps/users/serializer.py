from rest_framework import serializers
from . import models
import re
from django.contrib.auth.hashers import make_password

class RegisterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["firstName", "lastName", "address", "email", "password"]
        
        
    def validate_password(self, value):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter, "
                "one uppercase letter, one number, and one special character, "
                "and must be at least 8 characters long."
            )

        return value

    
    def validate_firstName(self, value):
        if len(value) < 1:
            raise serializers.ValidationError(
                "There must be firstname."
            )
        return value
    
    def validate_lastName(self, value):
        if len(value) < 1:
            raise serializers.ValidationError(
                "There must be lastname"
            )
        return value
    
    def validate_address(self, value):
        if len(value) < 5:
            raise serializers.ValidationError(
                "Address must contain 5 characters."
            )
        return value
    
    #For the password hashing
    def create(self, validated_data):
        # generate the hash of the password
        validated_data["password"] = make_password(
            validated_data["password"]
        )
        return models.User.objects.create(
            **validated_data
        )