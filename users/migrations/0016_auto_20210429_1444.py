# Generated by Django 3.1.7 on 2021-04-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_playlist_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='name_playlist',
            field=models.CharField(max_length=30, null=True, verbose_name='Name Playlist'),
        ),
        migrations.AlterUniqueTogether(
            name='playlist',
            unique_together={('user_name', 'name_playlist')},
        ),
    ]
