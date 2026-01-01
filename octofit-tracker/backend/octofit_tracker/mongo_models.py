from mongoengine import Document, StringField, EmailField, IntField, DateField, ReferenceField

class Team(Document):
    name = StringField(required=True, unique=True, max_length=50)
    description = StringField()

class User(Document):
    email = EmailField(required=True, unique=True)
    name = StringField(required=True, max_length=100)
    team = ReferenceField(Team)

class Workout(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    difficulty = StringField(max_length=20)

class Activity(Document):
    user = ReferenceField(User)
    type = StringField(max_length=50)
    duration = IntField()  # in minutes
    date = DateField()

class Leaderboard(Document):
    user = ReferenceField(User)
    score = IntField()
    rank = IntField()
