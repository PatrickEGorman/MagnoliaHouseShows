# Generated by Django 2.2.3 on 2019-07-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Minimum'), (4, 'Low'), (3, 'Average'), (2, 'High'), (1, 'Maxiumum')], default=3),
        ),
        migrations.AlterField(
            model_name='artist',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Minimum'), (4, 'Low'), (3, 'Average'), (2, 'High'), (1, 'Maxiumum')], default=3),
        ),
        migrations.AlterField(
            model_name='genre',
            name='priority',
            field=models.IntegerField(choices=[(5, 'Minimum'), (4, 'Low'), (3, 'Average'), (2, 'High'), (1, 'Maxiumum')], default=3),
        ),
    ]
