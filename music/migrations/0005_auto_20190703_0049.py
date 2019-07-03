# Generated by Django 2.2.3 on 2019-07-03 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_album_release_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('hometown', models.TextField(blank=True, default='')),
                ('bandcamp', models.URLField(blank=True, default='')),
                ('youtube', models.URLField(blank=True, default='')),
                ('facebook', models.URLField(blank=True, default='')),
                ('soundcloud', models.URLField(blank=True, default='')),
            ],
        ),
        migrations.RemoveField(
            model_name='band',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='band',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='music.Album'),
        ),
    ]
