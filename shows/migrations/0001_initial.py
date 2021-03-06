# Generated by Django 2.2.3 on 2019-07-19 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(default='08:00')),
                ('suggested_donation', models.IntegerField(default=7)),
                ('suggested_donation_max', models.IntegerField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, default='')),
                ('instagram', models.URLField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('priority', models.IntegerField(choices=[(1, 'Minimum'), (2, 'Low'), (3, 'Average'), (4, 'High'), (5, 'Maxiumum')], default=3)),
                ('artists', models.ManyToManyField(to='music.Artist')),
                ('genres', models.ManyToManyField(blank=True, to='music.Genre')),
                ('metaData', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.MetaData')),
            ],
            options={
                'ordering': ['priority', '-date'],
            },
        ),
    ]
