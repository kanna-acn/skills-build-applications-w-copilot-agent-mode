from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='dc')

        # Activities
        Activity.objects.create(user=tony.email, type='run', duration=30, date='2026-01-01')
        Activity.objects.create(user=steve.email, type='cycle', duration=45, date='2026-01-02')
        Activity.objects.create(user=bruce.email, type='swim', duration=60, date='2026-01-03')
        Activity.objects.create(user=clark.email, type='yoga', duration=20, date='2026-01-04')

        # Leaderboard
        Leaderboard.objects.create(user=tony.email, score=100)
        Leaderboard.objects.create(user=steve.email, score=90)
        Leaderboard.objects.create(user=bruce.email, score=110)
        Leaderboard.objects.create(user=clark.email, score=95)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Squats', description='Do 40 squats')
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
