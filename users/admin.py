from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.db import models

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Song, Playlist, Artist, Playlist_Songs


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name', 'birthday', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'birthday', 'password', 'cache')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'birthday', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

class SongAdmin(admin.ModelAdmin):
    model = Song
    list_display = ('name_song',)

class PlaylistAdmin(admin.ModelAdmin):
    model = Playlist
    list_display = ('name_playlist',)

class ArtistAdmin(admin.ModelAdmin):
    model = Artist
    list_display = ('name_artist', 'info_artist')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Song)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Playlist_Songs)




