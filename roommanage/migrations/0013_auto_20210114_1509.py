# Generated by Django 3.1.5 on 2021-01-14 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0012_auto_20210114_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='payment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='arrivedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 15, 9, 46, 382526)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leavedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 15, 9, 46, 382526)),
        ),
    ]