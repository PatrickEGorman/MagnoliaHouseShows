# Generated by Django 2.2.3 on 2019-07-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_artist_bandcamp_embed_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='soundcloud_embed_code',
            field=models.TextField(blank=True, default=''),
        ),
    ]
