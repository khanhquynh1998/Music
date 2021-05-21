from django.shortcuts import render
from django.http import HttpResponse
from users.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from users.models import Song, Artist, Playlist, Playlist_Songs, Comments

from .predict_cmts import toxicity_level

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
    #print(name_type)
    if(name_type == None):
        song = Song.objects.all()
    else:
        song = Song.objects.filter(name_type=name_type)
    #print(song)
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
    vpop = Song.objects.filter(name_type='vpop')
    kpop = Song.objects.filter(name_type='kpop')
    usuk = Song.objects.filter(name_type='usuk')
    tmp_Vpop = []
    tmp_Kpop = []
    tmp_USUK = []
    top_song_Vpop = []
    top_song_Kpop = []
    top_song_USUK = []
    for song in vpop:
        tmp_Vpop.append(song.listen_count)
    for song in kpop:
        tmp_Kpop.append(song.listen_count)
    for song in usuk:
        tmp_USUK.append(song.listen_count)
    tmp_Vpop.sort(reverse=True)
    tmp_Kpop.sort(reverse=True)
    tmp_USUK.sort(reverse=True)
    
    for i in range(len(vpop)):
        for song in vpop:
            if (song.listen_count == tmp_Vpop[i]) and song not in top_song_Vpop:
                top_song_Vpop.append(song)
    for i in range(len(kpop)):
        for song in kpop:
            if (song.listen_count == tmp_Kpop[i]) and song not in top_song_Kpop:
                top_song_Kpop.append(song)
    for i in range(len(usuk)):
        for song in usuk:
            if (song.listen_count == tmp_USUK[i]) and song not in top_song_USUK:
                top_song_USUK.append(song)
    
    return render(request, "ranking.html", {'top_song_Vpop': top_song_Vpop, 'top_song_Kpop': top_song_Kpop, 'top_song_USUK': top_song_USUK})

def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    song.listen_count += 1
    song.save()
    username = request.user.username
    datetime = str(timezone.now())
    date = datetime.split(' ')[0]
    time = datetime.split(' ')[1]
    value = {
        'time': time,
        'song_id': song_id
    }
    if(request.user.is_anonymous == False):
        if(request.user.cache['data'] == ''):
            #print("Init")
            request.user.cache['data'] = {
                'date_'+date: {
                    'time': time,
                    'song_id': song_id
                }
            }
            #print(request.user.cache)
            request.user.save()
        else: 
            #print(request.user.cache)
            #if(str('date_'+date) in request.user.cache['data']):
            append_value(request.user.cache['data'], 'date_'+date, value)
            #print(request.user.cache)
            request.user.save()
    comments = Comments.objects.filter(song=song_id)
    if request.method == 'POST':
        comment = request.POST.get('cmt','')
        if(toxicity_level(comment) == 1):
            comment_object = Comments.objects.create(uploaded_user=request.user,song=song, comment=comment)
            comment_object.save()
            if comment_object != None:
                return HttpResponse("<script>alert(\"Comment Uploaded\");window.location.href = window.location;</script>")
        else:
            return HttpResponse("<script>alert(\"Toxic Comments are not allowed!\");window.location.href = window.location;</script>")
    return render(request, "song_detail.html", {'song': song, 'username': username, 'comments': comments})

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