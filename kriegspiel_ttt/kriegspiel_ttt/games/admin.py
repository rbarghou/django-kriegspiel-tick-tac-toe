from django.contrib import admin

from .models import Game
from .forms import GameForm


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
    # form = GameForm
