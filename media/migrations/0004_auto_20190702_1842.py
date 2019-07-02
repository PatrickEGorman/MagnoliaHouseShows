# Generated by Django 2.2.3 on 2019-07-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_auto_20190702_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='flier',
            name='caption',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='flier',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='youtubevideo',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
