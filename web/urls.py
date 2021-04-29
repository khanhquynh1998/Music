from django.urls import path
from web import views

urlpatterns = [
    path('artists/', views.artist,name='artist'),
    path('songs/', views.song,name='song'),
    path('playlists/', views.playlist, name='playlist'),
    path('ranking/', views.rank,name='rank'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('playlists/<int:playlist_id>', views.playlist_detail, name='playlist_detail'),
]