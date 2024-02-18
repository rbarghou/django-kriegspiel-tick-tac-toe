from rest_framework import serializers

from kriegspiel_ttt.games.models import Game as _Game


class GameSerializer(serializers.ModelSerializer[_Game]):
    class Meta:
        model = _Game
        fields = ["player_O", "player_O", "game_data"]
