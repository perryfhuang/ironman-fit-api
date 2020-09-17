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
    id = serializers.IntegerField()

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'type', 'distance', 'time', 'exercise_1', 'exercise_1_weight', 'exercise_1_sets', 'exercise_1_reps', 'exercise_2', 'exercise_2_weight', 'exercise_2_sets', 'exercise_2_reps', 'exercise_3', 'exercise_3_weight', 'exercise_3_sets', 'exercise_3_reps', 'exercise_4', 'exercise_4_weight', 'exercise_4_sets', 'exercise_4_reps', 'exercise_5', 'exercise_5_weight', 'exercise_5_sets', 'exercise_5_reps',  'exercise_6', 'exercise_6_weight', 'exercise_6_sets', 'exercise_6_reps',  'exercise_7', 'exercise_7_weight', 'exercise_7_sets', 'exercise_7_reps', 'exercise_8', 'exercise_8_weight', 'exercise_8_sets', 'exercise_8_reps', 'exercise_9', 'exercise_9_weight', 'exercise_9_sets', 'exercise_9_reps', 'exercise_10', 'exercise_10_weight', 'exercise_10_sets', 'exercise_10_reps','caption', 'feeling', 'created_at', 'updated_at', 'owner')

class ShowWorkoutSerializer(serializers.ModelSerializer):
    owner = OwnerReadSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = ('id', 'type', 'distance', 'time', 'exercise_1', 'exercise_1_weight', 'exercise_1_sets', 'exercise_1_reps', 'exercise_2', 'exercise_2_weight', 'exercise_2_sets', 'exercise_2_reps', 'exercise_3', 'exercise_3_weight', 'exercise_3_sets', 'exercise_3_reps', 'exercise_4', 'exercise_4_weight', 'exercise_4_sets', 'exercise_4_reps', 'exercise_5', 'exercise_5_weight', 'exercise_5_sets', 'exercise_5_reps',  'exercise_6', 'exercise_6_weight', 'exercise_6_sets', 'exercise_6_reps',  'exercise_7', 'exercise_7_weight', 'exercise_7_sets', 'exercise_7_reps', 'exercise_8', 'exercise_8_weight', 'exercise_8_sets', 'exercise_8_reps', 'exercise_9', 'exercise_9_weight', 'exercise_9_sets', 'exercise_9_reps', 'exercise_10', 'exercise_10_weight', 'exercise_10_sets', 'exercise_10_reps','caption', 'feeling', 'created_at', 'updated_at', 'owner')

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
