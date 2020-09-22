from django.urls import path
from .views.workout_views import Workouts, CreateWorkout, WorkoutDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword, UserInfo, UpdateUserInfo, UsersInfo

urlpatterns = [
  	# Restful routing
    path('workouts/', Workouts.as_view(), name='workouts'),
    path('create-workout/', CreateWorkout.as_view(), name='create-workout'),
    path('workouts/<int:pk>/', WorkoutDetail.as_view(), name='workout_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
    path('users/', UsersInfo.as_view(), name='users-all'),
    path('users/<int:pk>/', UserInfo.as_view(), name='users'),
    path('update-profile/<int:pk>/', UpdateUserInfo.as_view(), name='update-user')
]
