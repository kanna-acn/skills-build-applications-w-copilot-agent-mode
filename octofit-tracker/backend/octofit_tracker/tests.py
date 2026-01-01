from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email='test@example.com', name='Test User', team='marvel')
        self.assertEqual(user.email, 'test@example.com')
    def test_team_creation(self):
        team = Team.objects.create(name='marvel')
        self.assertEqual(team.name, 'marvel')
    def test_activity_creation(self):
        activity = Activity.objects.create(user='test@example.com', type='run', duration=30, date='2026-01-01')
        self.assertEqual(activity.type, 'run')
    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='test@example.com', score=100)
        self.assertEqual(lb.score, 100)
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.assertEqual(workout.name, 'Pushups')
