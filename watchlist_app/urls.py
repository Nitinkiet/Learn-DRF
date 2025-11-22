from django.urls import path
from . import views


urlpatterns = [
    path('watchlist/', views.WatchlistAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', views.WatchDetailAV.as_view(), name='watchlist-detail'),
    path('platform/', views.StreamPlatformAV.as_view(), name='watch-list'),
    path('platform/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='watchlist-detail'),
]