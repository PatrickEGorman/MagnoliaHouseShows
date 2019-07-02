# Generated by Django 2.2.3 on 2019-07-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('cover_image', models.ImageField(blank=True, upload_to='')),
                ('band_camp', models.URLField(default='')),
                ('youtube', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('sub_genres', models.ManyToManyField(blank=True, null=True, related_name='_genre_sub_genres_+', to='music.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('genres', models.ManyToManyField(blank=True, to='music.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('home_town', models.TextField(default='')),
                ('band_camp', models.URLField(default='')),
                ('youtube', models.URLField(default='')),
                ('facebook', models.URLField(default='')),
                ('soundcloud', models.URLField(default='')),
                ('albums', models.ManyToManyField(blank=True, to='music.Album')),
                ('genres', models.ManyToManyField(to='music.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(blank=True, to='music.Genre'),
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(blank=True, to='music.Song'),
        ),
    ]
