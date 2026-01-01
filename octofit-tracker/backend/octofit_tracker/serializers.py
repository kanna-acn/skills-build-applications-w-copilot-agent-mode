from rest_framework import serializers
from .mongo_models import User, Team, Activity, Workout, Leaderboard

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(allow_blank=True, required=False)

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    team = serializers.CharField(allow_blank=True, required=False)

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, required=False)
    difficulty = serializers.CharField(max_length=20)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()
    date = serializers.DateField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    score = serializers.IntegerField()
    rank = serializers.IntegerField()
