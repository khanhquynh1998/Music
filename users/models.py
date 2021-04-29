import base64

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import JSONField 
from django.contrib.postgres.fields import ArrayField



from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_("username"), max_length=20, null=True)
    first_name = models.CharField(_("first name"), max_length=20, null= True)
    last_name = models.CharField(_("last name"), max_length=20, null= True)
    birthday = models.DateField(null= True)
    image_user = models.ImageField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    cache = JSONField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'birthday']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Artist(models.Model):
    #id_artist = models.CharField(_("ID Artist"), max_length=20, unique=True) 
    name_artist = models.CharField(_("Name Artist"), max_length=40, null=True) 
    info_artist = models.CharField(_("Infomation"), max_length=50, null=True)
    image_artist = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name_artist

    def imageURL(self):
        try:
            url = self.image_artist.url
        except:
            url = ''
        return url
     

class Song(models.Model):
    #id_song = models.CharField(_("ID song"), unique=True, max_length=20)
    TYPE_CHOICE = (
    ('Vpop','Vpop'),
    ('Kpop','Kpop'),
    ('USUK','USUK'),
    )
    name_song = models.CharField(_("Name song"), max_length=50, null=True)
    aritst = models.ForeignKey(Artist, on_delete = models.CASCADE, null=True)
    image_song = models.ImageField(null=True, blank=True)
    audio = models.FileField(null = True, blank=True)
    name_type = models.CharField(max_length=20, choices= TYPE_CHOICE, null=True, blank=True )
    date_joined = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name_song

    def audioURL(self):
        try:
           url = self.audio.url
        except:
            url = ''
        return url

    def imageURL(self):
        try:
            url = self.image_song.url
        except:
            url = ''
        return url
    
class Playlist(models.Model):
    #id_playlist = models.CharField(_("ID Playlist"), max_length=30, unique=True) 
    name_playlist = models.CharField(_("Name Playlist"), max_length=30, null=True)
    image_playlist = models.ImageField(null=True, blank=True)
    user_name = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null=True)
    song_list = ArrayField(models.OneToOneField(Song, on_delete = models.CASCADE, blank=True, null=True))
    def __str__(self):
        return self.name_playlist
    class Meta:
        unique_together = ('user_name','name_playlist',)






     



    

