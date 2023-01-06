from django.urls import include, path

from . import views
from .router import router

urlpatterns = [
    path('' , include(router.urls)),
    path('item/<int:pk>/', views.MusicDetail.as_view()),
    path('itemlist/<int:pk>/', views.GenresDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
