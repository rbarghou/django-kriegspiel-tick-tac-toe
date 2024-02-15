from django.conf import settings
from django.db import models
from django.db.models import F, Q


from .gameboard import GameBoard


class GameDataField(models.JSONField):

    def from_db_value(self, value, expression, connection):
        value = super().from_db_value(value, expression, connection)
        if value is None or isinstance(value, GameBoard):
            return value
        return GameBoard.from_dict(value)

    def to_python(self, value):
        value = super().to_python(value)
        if value is None or isinstance(value, GameBoard):
            return value
        return GameBoard.from_dict(value)

    def get_prep_value(self, value):
        if isinstance(value, GameBoard):
            value = value.to_dict()
        return super().get_prep_value(value)


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
    game_data = GameDataField(null=False, default={})

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
