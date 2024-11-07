from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)



class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


    def validate_username(self, username):
        if not username.isalnum():
          raise serializers.ValidationError("Username should only contain alphanumeric characters.")
        return username
