from rest_framework import serializers
from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)


    class Meta:
        model = User
        fields = ('email','password', 'password_confirm', 'is_mentor')

    def validate(self, attrs):
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')

        if pass1 != pass2:
            raise serializers.ValidationError("Password don't match")
        
        return attrs
    
    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user with this email already exists")
        
        return email

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ["id","is_superuser","is_staff","is_active","email","first_name","last_name","experience","is_mentor","photo"]
