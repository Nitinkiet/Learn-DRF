from django.urls import path
from . import views


urlpatterns = [
    path('watchlist/', views.WatchlistAV.as_view(), name='watch-list'),
    path('watchlist/<int:pk>/', views.WatchDetailAV.as_view(), name='watchlist-detail'),
    path('platform/', views.StreamPlatformAV.as_view(), name='watch-list'),
    path('platform/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='watchlist-detail'),
    
    path('platform/<int:pk>/review/', views.ReviewList.as_view(), name='review-list'),
    path('platform/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('platform/review/<int:pk>/',views.ReviewDetail.as_view(),name='review-detail'),
   
]