# Generated by Django 3.1.5 on 2021-01-14 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0018_auto_20210114_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='arrivedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 19, 57, 6, 187678)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leavedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 19, 57, 6, 187678)),
        ),
    ]