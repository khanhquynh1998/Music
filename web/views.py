from django.shortcuts import render
from django.http import HttpResponse
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from users.models import Song, Artist, Playlist, Playlist_Songs

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def append_value(dic_obj, key, value):
    if key in dic_obj:
        if not isinstance(dic_obj[key], list):
            dic_obj[key] = [dic_obj[key]]
        dic_obj[key].append(value)
    else:
        dic_obj[key] = value

def dashboard(request):
    songs = Song.objects.all()
    song = []
    rcm = []
    for i in songs:
        if i.was_uploaded_recently():
            song.append(i)
        if i.listen_count > 0:
            rcm.append(i)
    song = song[0:4]
    rcm = rcm[0:4]
    vpop = Song.objects.filter(name_type='vpop')
    kpop = Song.objects.filter(name_type='kpop')
    usuk = Song.objects.filter(name_type='usuk')
    return render(request,'dashboard.html',{'song': song,'rcm': rcm, 'vpop': vpop, 'kpop': kpop, 'usuk': usuk})

def artist(request):
    artist = Artist.objects.all()
    return render(request, "artist.html",{'artist': artist})

def song(request):
    name_type = request.GET.get('name_type')
    print(name_type)
    if(name_type == None):
        song = Song.objects.all()
    else:
        song = Song.objects.filter(name_type=name_type)
    print(song)
    return render(request, "song.html",{'song': song})

def playlist(request):
    playlist = Playlist.objects.all()
    pl_song = Playlist_Songs.objects.all()
    #for i in playlist:
    #    tmp = Playlist_Songs.objects.filter(playlist_id=i.id)
    #    pl_song.append(tmp)
    #    print(tmp)
    return render(request, "playlist.html", {'playlists': playlist, 'pl_songs': pl_song})

def rank(request):
    return render(request, "ranking.html")

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    username = request.user.username
    datetime = str(timezone.now())
    date = datetime.split(' ')[0]
    time = datetime.split(' ')[1]
    value = {
        'time': time,
        'song_id': song_id
    }
    if(request.user.cache['data'] == ''):
        print("Init")
        request.user.cache['data'] = {
            'date_'+date: {
                'time': time,
                'song_id': song_id
            }
        }
        print(request.user.cache)
        request.user.save()
    else: 
        print(request.user.cache)
        #if(str('date_'+date) in request.user.cache['data']):
        append_value(request.user.cache['data'], 'date_'+date, value)
        print(request.user.cache)
        request.user.save()
    return render(request, "song_detail.html", {'song': song, 'username': username})

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