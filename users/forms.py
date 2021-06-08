from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, Song, Playlist, Artist


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'birthday')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'birthday')

class SongCreationForm(ModelForm):
    class Meta:
        model = Song
        fields = ('name_song', 'aritst', 'image_song', 'audio', 'name_type', 'upload_by')

class ArtistCreationForm(ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        
class PlaylistCreationForm(ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'