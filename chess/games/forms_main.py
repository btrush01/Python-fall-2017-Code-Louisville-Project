from django import forms
from .models import Game


result_possibilities= [
    ('won', 'Won'),
    ('lost', 'Lost'),
    ('drew', 'Drew'),
    ]

color_possibilities= [
    ('white', 'White'),
    ('black', 'Black')
    ]

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['player', 'opponent', 'color', 'result', 'created_at']

class Game(forms.Form):
    player= forms.CharField(max_length=30)
    opponent= forms.CharField(max_length=30)
    color= forms.Charfield(label='What color did you play?', widget=forms.RadioSelect(choices=color_possibilities))
    result= forms.CharField(label='What was your outcome?', widget=forms.RadioSelect(choices=result_possibilities))
    created_at = models.DateTimeField(auto_now_add=True)