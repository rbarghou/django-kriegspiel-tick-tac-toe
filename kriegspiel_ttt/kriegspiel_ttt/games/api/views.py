from rest_framework.utils.encoders import JSONEncoder
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import GenericViewSet

from .serializers import GameSerializer as _GameSerializer


from kriegspiel_ttt.games.models import Game as _Game
from kriegspiel_ttt.games.gameboard import GameBoard as _GameBoard



class GameJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, _GameBoard):
            obj = obj.to_dict()
        return super().default(obj)


class GameJSONRenderer(JSONRenderer):
    encoder_class = GameJSONEncoder


class GameViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = _GameSerializer
    queryset = _Game.objects.all()
    renderer_classes = [GameJSONRenderer] + GenericViewSet.renderer_classes
