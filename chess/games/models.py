from django.db import models
from django import forms
from .forms_main import color_possibilities, result_possibilities

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=30, unique=True)
    rating = models.IntegerField






class Game_History(models.Model):
    player_1 = .name
    player_2 = .name
    result =
    created_at = models.DateTimeField()

