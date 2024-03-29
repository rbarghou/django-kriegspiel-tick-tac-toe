# Generated by Django 4.2.10 on 2024-02-11 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("started", models.DateTimeField(auto_now_add=True)),
                ("completed", models.DateTimeField(null=True)),
                ("game_data", models.JSONField(default={})),
                (
                    "player_O",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="O_game_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "player_X",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="X_game_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.CheckConstraint(
                check=models.Q(("player_X", models.F("player_O")), _negated=True), name="games_game_different_players"
            ),
        ),
        migrations.AddConstraint(
            model_name="game",
            constraint=models.CheckConstraint(
                check=models.Q(("started__lte", models.F("completed"))),
                name="games_game_game_started_before_completed",
            ),
        ),
    ]
