# Generated by Django 2.2.3 on 2019-08-01 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20190720_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
