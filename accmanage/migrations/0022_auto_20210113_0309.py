# Generated by Django 3.1.5 on 2021-01-13 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0021_auto_20210113_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userage',
            field=models.IntegerField(default=0),
        ),
    ]
