from django.conf import settings
from django.db import models
from django.db.models import F, Q


from .gameboard import GameBoard as _GameBoard


class Game(models.Model):
    started = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True)
    player_X = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
        related_name="X_game_set"
    )
    player_O = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
        related_name="O_game_set"
    )
    game_data = models.JSONField(null=False, default={}, encoder=_GameBoard.Encoder, decoder=_GameBoard.Decoder)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(player_X=F("player_O")),
                name="%(app_label)s_%(class)s_different_players"
            ),
            models.CheckConstraint(
                check=Q(started__lte=F("completed")),
                name="%(app_label)s_%(class)s_game_started_before_completed"
            )
        ]
