# Generated by Django 3.2 on 2021-05-01 15:58

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210501_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cache',
            field=models.JSONField(default=users.models.default_cache),
        ),
    ]
