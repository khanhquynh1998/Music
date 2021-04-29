from django.shortcuts import render
from django.http import HttpResponse
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from users.models import Song, Artist, Playlist, Playlist_Songs

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def dashboard(request):
    song = Song.objects.all()
    song = song[0:4]
    #song_artist = song.aritst_id
    return render(request,'dashboard.html',{'song': song})

def artist(request):
    artist = Artist.objects.all()
    return render(request, "artist.html",{'artist': artist})

def song(request):
    song = Song.objects.all()
    return render(request, "song.html",{'song': song})

def playlist(request):
    playlist = Playlist.objects.all()
    return render(request, "playlist.html", {'playlists': playlist})

def rank(request):
    return render(request, "ranking.html")

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, "song_detail.html", {'song': song})

def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    songs_of_artist = Song.objects.filter(aritst=artist_id)
    return render(request, "artist_detail.html", {'artist': artist, 'songs': songs_of_artist,})

def playlist_detail(request, playlist_id):
    pl = Playlist_Songs.objects.filter(playlist_id=playlist_id)
    playlist = pl[0]
    song = Playlist_Songs.objects.filter(playlist_id=playlist_id)
    song_url = []
    for i in song:
        song_url.append(i.song.audioURL)
    return render(request, "playlist_detail.html", {'playlist': playlist, 'songs': song, 'song_url': song_url})