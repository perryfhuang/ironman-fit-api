from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.workout import Workout
from .models.user import User

class OwnerReadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    pro_pic = serializers.URLField(max_length=999)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    bio = serializers.CharField(max_length=280)
    gender = serializers.CharField(max_length=100)
    height = serializers.IntegerField()
    weight = serializers.IntegerField()

class WorkoutSerializer(serializers.ModelSerializer):
    owner = OwnerReadSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = '__all__'
        # fields = ('id', 'type', 'distance', 'time', 'caption', 'feeling', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserLoginSerializer(UserSerializer):
    # Require email, password for sign in
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
