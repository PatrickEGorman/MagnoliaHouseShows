# Generated by Django 2.2.3 on 2019-07-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
        ('media', '__first__'),
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='shows',
            field=models.ManyToManyField(blank=True, to='shows.Show'),
        ),
        migrations.AddField(
            model_name='history',
            name='youtube_videos',
            field=models.ManyToManyField(blank=True, max_length=2, to='media.YoutubeVideo'),
        ),
    ]
