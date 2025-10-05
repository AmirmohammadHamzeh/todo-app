from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """ساخت یوزر با CustomUserManager"""
        validated_data.pop('confirm_password')  # نیازی به ذخیره‌اش نیست
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # اضافه کردن فیلدهای دلخواه به payload
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['full_name'] = user.full_name
        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            try:
                u = CustomUser.objects.get(email=email)
                raise serializers.ValidationError("Password is incorrect")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("No user with this email")

        if not user.is_active:
            raise serializers.ValidationError("This account is inactive")

        data = super().validate(attrs)
        return data
