from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.workout import Workout
from ..serializers import WorkoutSerializer, ShowWorkoutSerializer, UserSerializer

# Create your views here.
class Workouts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = WorkoutSerializer
    def get(self, request):
        """Index request"""
        # Get all the mangos:
        workouts = Workout.objects.all()
        # Filter the mangos by owner, so you can only see your owned mangos
        # workouts = Workout.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ShowWorkoutSerializer(workouts, many=True).data
        return Response({ 'workouts': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['workout']['owner'] = request.user.id
        # Serialize/create mango
        workout = WorkoutSerializer(data=request.data['workout'])
        # If the mango data is valid according to our serializer...
        if workout.is_valid():
            # Save the created mango & send a response
            workout.save()
            return Response({ 'workout': workout.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(workout.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        workout = get_object_or_404(Workout, pk=pk)
        # Only want to show owned mangos?
        # if not request.user.id == workout.owner.id:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        data = ShowWorkoutSerializer(workout).data
        return Response({ 'workout': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        workout = get_object_or_404(Workout, pk=pk)
        # Check the mango's owner agains the user making this request
        if not request.user.id == workout.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['mango'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['workout'].get('owner', False):
            del request.data['workout']['owner']

        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        workout = get_object_or_404(Workout, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == workout.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this workout')

        # Add owner to data object now that we know this user owns the resource
        request.data['workout']['owner'] = request.user.id
        # Validate updates with serializer
        data = WorkoutSerializer(workout, data=request.data['workout'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
