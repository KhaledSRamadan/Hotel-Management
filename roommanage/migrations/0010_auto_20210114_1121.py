# Generated by Django 3.1.5 on 2021-01-14 09:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0009_auto_20210114_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='arrivedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 14, 11, 21, 43, 328759)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leavedate',
            field=models.DateField(default=datetime.datetime(2021, 1, 16, 11, 21, 43, 328759)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='roomid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roommanage.room'),
        ),
    ]