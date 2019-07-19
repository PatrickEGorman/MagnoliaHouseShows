# Generated by Django 2.2.3 on 2019-07-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        ('main', '0001_initial'),
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_url', models.URLField()),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('caption', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(choices=[(1, 'Minimum'), (2, 'Low'), (3, 'Average'), (4, 'High'), (5, 'Maxiumum')], default=3)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='music.Artist')),
                ('metaData', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.MetaData')),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='shows.Show')),
            ],
            options={
                'ordering': ['priority', 'date', 'show', 'artist'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('caption', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(choices=[(1, 'Minimum'), (2, 'Low'), (3, 'Average'), (4, 'High'), (5, 'Maxiumum')], default=3)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='music.Artist')),
                ('metaData', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.MetaData')),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='shows.Show')),
            ],
            options={
                'ordering': ['priority', 'date', 'show', 'artist'],
            },
        ),
        migrations.CreateModel(
            name='Flier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(default=None)),
                ('caption', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(choices=[(1, 'Minimum'), (2, 'Low'), (3, 'Average'), (4, 'High'), (5, 'Maxiumum')], default=3)),
                ('metaData', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.MetaData')),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fliers', to='shows.Show')),
            ],
            options={
                'ordering': ['priority', 'date', 'show'],
            },
        ),
    ]
