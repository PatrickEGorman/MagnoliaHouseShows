# Generated by Django 2.2.3 on 2019-08-01 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20190801_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Minimum'), (4, 'Low'), (3, 'Average'), (2, 'High'), (1, 'Maxiumum')], default=3),
        ),
    ]
