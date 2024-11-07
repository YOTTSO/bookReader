from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from .models import UserProfile


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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['display_name', 'profile_picture']

    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)

        if 'profile_picture' in validated_data:
            instance.save()

        instance.save()
        return instance
