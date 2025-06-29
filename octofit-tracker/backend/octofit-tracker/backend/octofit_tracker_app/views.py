from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

CODESPACE_URL = "https://special-rotary-phone-q76549j4p7943qpx-8000.app.github.dev"
LOCAL_URL = "http://localhost:8000"

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': f'{CODESPACE_URL}/api/users/',
        'teams': f'{CODESPACE_URL}/api/teams/',
        'activities': f'{CODESPACE_URL}/api/activities/',
        'leaderboard': f'{CODESPACE_URL}/api/leaderboard/',
        'workouts': f'{CODESPACE_URL}/api/workouts/',
        'local_users': f'{LOCAL_URL}/api/users/',
        'local_teams': f'{LOCAL_URL}/api/teams/',
        'local_activities': f'{LOCAL_URL}/api/activities/',
        'local_leaderboard': f'{LOCAL_URL}/api/leaderboard/',
        'local_workouts': f'{LOCAL_URL}/api/workouts/',
    })
