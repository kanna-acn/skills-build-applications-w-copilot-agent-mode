from django.core.management.base import BaseCommand
from octofit_tracker.mongo_models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data (MongoEngine)'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.delete()
        Activity.objects.delete()
        Workout.objects.delete()
        User.objects.delete()
        Team.objects.delete()

        # Create Teams
        marvel = Team(name='marvel', description='Marvel Team').save()
        dc = Team(name='dc', description='DC Team').save()

        # Create Users
        tony = User(email='tony@stark.com', name='Tony Stark', team=marvel).save()
        steve = User(email='steve@rogers.com', name='Steve Rogers', team=marvel).save()
        bruce = User(email='bruce@wayne.com', name='Bruce Wayne', team=dc).save()
        clark = User(email='clark@kent.com', name='Clark Kent', team=dc).save()

        # Create Workouts
        pushups = Workout(name='Pushups', description='Do 50 pushups', difficulty='easy').save()
        running = Workout(name='Running', description='Run 5km', difficulty='medium').save()

        # Create Activities
        Activity(user=tony, type='pushups', duration=20, date=date.today()).save()
        Activity(user=steve, type='running', duration=30, date=date.today()).save()
        Activity(user=bruce, type='pushups', duration=25, date=date.today()).save()
        Activity(user=clark, type='running', duration=35, date=date.today()).save()

        # Create Leaderboard
        Leaderboard(user=tony, score=200, rank=1).save()
        Leaderboard(user=steve, score=180, rank=2).save()
        Leaderboard(user=bruce, score=170, rank=3).save()
        Leaderboard(user=clark, score=160, rank=4).save()

        self.stdout.write(self.style.SUCCESS('Test data populated successfully (MongoEngine).'))
