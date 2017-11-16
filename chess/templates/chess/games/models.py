from django.db import models
from . import glicko2

# Create your models here.


class Player(models.Model):
    id = models.()
    name = models.CharField(max_length=30, unique=True)
    rating = models.()


class Game(models.Model):
    id = models.()
    created_at = models.DateTimeField(auto_now_add=True)
    result = bool()


class Game_History(models.Model):
    id =
    player_1 = .name
    player_2 = .name
    result =
    created_at = models.DateTimeField()
