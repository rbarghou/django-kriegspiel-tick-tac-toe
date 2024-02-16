from django import forms

from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "player_X",
            "player_O",
            "game_data"
        ]
