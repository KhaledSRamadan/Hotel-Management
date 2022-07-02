# Generated by Django 3.1.5 on 2021-01-13 00:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0019_auto_20210113_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userage',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(18)]),
        ),
    ]
