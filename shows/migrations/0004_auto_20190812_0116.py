# Generated by Django 2.2.3 on 2019-08-12 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_show_cancelled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
