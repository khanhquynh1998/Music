# Generated by Django 3.2 on 2021-04-29 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_remove_playlist_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist_songs',
            name='playlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.playlist'),
        ),
    ]
