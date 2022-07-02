# Generated by Django 3.1.5 on 2021-01-12 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0004_customuser_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userage',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AddField(
            model_name='customuser',
            name='usercreditcard',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AddField(
            model_name='customuser',
            name='userphone',
            field=models.IntegerField(null=True),
        ),
    ]
