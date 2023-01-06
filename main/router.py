from rest_framework import routers

from .views import genre_viewset, music_viewset

router=routers.DefaultRouter()
router.register('MusicModel',music_viewset)
router.register('Genres',genre_viewset)
