from os import name
from django.conf.urls import url
from django.urls import path, include
from web import views

urlpatterns = [
    path('identicon/', include('django_pydenticon.urls')),
    path('song_upload/', views.song_upload, name='upload_song'),
    path('song_create/', views.createSong, name='createSong'),
    path('artist_create/', views.createArtist, name='createArtist'),
    path('artist_form/', views.artist_form, name='artist_form'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_update/<str:pk>', views.updateUser, name='update_user'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('artists/', views.artist,name='artist'),
    path('songs/', views.song,name='song'),
    path('playlists/', views.playlist, name='playlist'),
    path('ranking/', views.rank,name='rank'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('playlists/<int:playlist_id>', views.playlist_detail, name='playlist_detail'),
]