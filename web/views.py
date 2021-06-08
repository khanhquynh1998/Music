from django.db.models.fields.files import ImageField
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from users.models import *
from users.forms import *

from .predict_cmts import toxicity_level


def append_value(dic_obj, key, value):
    if key in dic_obj:
        if not isinstance(dic_obj[key], list):
            dic_obj[key] = [dic_obj[key]]
        dic_obj[key].append(value)
    else:
        dic_obj[key] = value

def user_profile(request):
    return render(request, 'user_profile.html')

def song_upload(request):
    form = SongCreationForm()
    return render(request, 'song_upload.html', {'form': form})

def artist_form(request):
    form = ArtistCreationForm()
    return render(request, 'artist_create.html', {'form': form})


def admin_dashboard(request):
    songList = Song.objects.all()
    playlistList = Playlist.objects.all()
    commentList = Comments.objects.all()
    userList = CustomUser.objects.all()
    artistList = Artist.objects.all()

    list = []
    for playlist in playlistList:
        tmp = []
        for song in Playlist_Songs.objects.filter(playlist=playlist):
            tmp.append(song)
        list.append([playlist, tmp, len(tmp)])
    
    context = {
        'songList': songList,
        'playlistList': list,
        'userList': userList,
        'artistList': artistList,
        'commentList': commentList
    }

    return render(request, 'admin_dashboard.html', context)

def dashboard(request):
    songs = Song.objects.all()
    song = Song.objects.order_by('-date_joined')
    rcm = Song.objects.order_by('-listen_count')

    song = song[0:4]
    rcm = rcm[0:4]

    vpop = Song.objects.filter(name_type='vpop')
    kpop = Song.objects.filter(name_type='kpop')
    usuk = Song.objects.filter(name_type='usuk')
    context = {
        'songList': songs,
        'song': song,
        'rcm': rcm,
        'vpop': vpop,
        'kpop': kpop,
        'usuk': usuk
    }
    return render(request,'dashboard.html', context)

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
    rcm = Song.objects.order_by('-listen_count')[0:4]
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
    return render(request, "song_detail.html", {'song': song, 'username': username, 'comments': comments, 'rcm': rcm})

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

def createSong(request):
    form = SongCreationForm()
    if request.method == 'POST':
        form = SongCreationForm(request.POST, request.FILES, upload_by=request.POST.user)
        if form.is_valid():
            form.save()
    return HttpResponse("<script>alert(\"Song Uploaded\");window.location.replace(\"/\");</script>")

def updateSong(request, pk):
    song = Song.objects.get(id=pk)
    form = SongCreationForm(instance=song)
    if request.method == 'POST':
        form = SongCreationForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            redirect('admin_dashboard.html')
    context = {'form': form}
    return render(request, 'registration/songCreation.html', context)

def deleteSong(request, pk):
    song = Song.objects.get(id=pk)
    context = {'item': song}
    if request.method == 'POST':
        song.delete()
        redirect('admin_dashboard.html')
    return render(request, 'registration/itemDelete.html', context)

def createArtist(request):
    form = ArtistCreationForm()
    if request.method == 'POST':
        form = ArtistCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
           return HttpResponse("<script>alert(\"Error! Try again later!\");window.location.href = window.location;</script>") 
    return HttpResponse("<script>alert(\"Artist Created!\");window.location.replace(\"/\");</script>")
#
#def updateArtist(request, pk):
#    artist = Artist.objects.get(id=pk)
#    form = ArtistCreationForm(instance=artist)
#    if request.method == 'POST':
#        form = ArtistCreationForm(request.POST, instance=artist)
#        if form.is_valid():
#            form.save()
#            redirect('admin_dashboard.html')
#    context = {'form': form}
#    return render(request, 'registration/songCreation.html', context)
#
#def deleteArtist(request, pk):
#    artist = Artist.objects.get(id=pk)
#    context = {'item': artist}
#    if request.method == 'POST':
#        artist.delete()
#        redirect('admin_dashboard.html')
#    return render(request, 'registration/itemDelete.html', context)
#
def updateUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    form = CustomUserChangeForm(instance=user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse("<script>alert(\"Updated!\");window.location.replace(\"/\");</script>")
        else:
           return HttpResponse("<script>alert(\"Error! Try again later!\");window.location.href = window.location;</script>") 

def deleteUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    context = {'item': user}
    if request.method == 'POST':
        user.delete()
        redirect('admin_dashboard.html')
    return render(request, 'registration/itemDelete.html', context)

def deleteComment(request, pk):
    comment = Comments.objects.get(id=pk)
    context = {'item': comment}
    if request.method == 'POST':
        comment.delete()
        redirect('admin_dashboard.html')
    return render(request, 'registration/itemDelete.html', context)