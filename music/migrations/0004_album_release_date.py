# Generated by Django 2.2.3 on 2019-07-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190702_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
