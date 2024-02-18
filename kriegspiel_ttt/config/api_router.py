from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from kriegspiel_ttt.users.api.views import UserViewSet
from kriegspiel_ttt.games.api.views import GameViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("games", GameViewSet)


app_name = "api"
urlpatterns = router.urls
