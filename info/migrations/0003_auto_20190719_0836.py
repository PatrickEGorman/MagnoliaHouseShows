# Generated by Django 2.2.3 on 2019-07-19 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20190719_0744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infopage',
            old_name='meta_data',
            new_name='metaData',
        ),
        migrations.RemoveField(
            model_name='history',
            name='fliers',
        ),
        migrations.RemoveField(
            model_name='history',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='history',
            name='youtube_videos',
        ),
    ]