def context(request):
    from users.models import Song, Playlist_Songs ,Playlist, Artist
    song = Song.objects.all()
    playlist = Playlist.objects.all()
    artist = Artist.objects.all()
    song_in_pl = Playlist_Songs.objects.all()
    context = {
        'context_song': song,
        'playlist': playlist,
        'artist': artist,
        'song_in_pl': song_in_pl
    }
    return context