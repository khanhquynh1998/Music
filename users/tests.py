import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Song


class SongModelTests(TestCase):

    def test_was_uploaded_recently_with_future_song(self):
        """
        was_uploaded_recently() returns False for songs whose date_joined
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_song = Song(date_joined=time)
        self.assertIs(future_song.was_uploaded_recently(), False)
    
    def test_was_uploaded_recently_with_old_song(self):
        """
        was_uploaded_recently() returns False for songs whose date_joined
        is older than 7 days.
        """
        time = timezone.now() - datetime.timedelta(days=7, seconds=1)
        old_song = Song(date_joined=time)
        self.assertIs(old_song.was_uploaded_recently(), False)

    def test_was_uploaded_recently_with_recent_song(self):
        """
        was_uploaded_recently() returns True for songs whose date_joined
        is within the last 7 days.
        """
        time = timezone.now() - datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)
        recent_song = Song(date_joined=time)
        self.assertIs(recent_song.was_uploaded_recently(), True)