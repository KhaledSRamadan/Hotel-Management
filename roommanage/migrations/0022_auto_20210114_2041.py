# Generated by Django 3.1.5 on 2021-01-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0021_auto_20210114_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='arrivedate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leavedate',
            field=models.DateField(),
        ),
    ]
