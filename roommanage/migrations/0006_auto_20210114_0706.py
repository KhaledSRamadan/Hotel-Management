# Generated by Django 3.1.5 on 2021-01-14 05:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0005_auto_20210114_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='arrivedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 7, 6, 10, 935309)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leavedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 7, 6, 10, 935309)),
        ),
    ]