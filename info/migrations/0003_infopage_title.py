# Generated by Django 2.2.3 on 2019-07-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20190702_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopage',
            name='title',
            field=models.TextField(blank=True, default=''),
        ),
    ]