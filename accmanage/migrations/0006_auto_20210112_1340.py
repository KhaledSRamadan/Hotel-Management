# Generated by Django 3.1.5 on 2021-01-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0005_auto_20210112_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userphone',
            field=models.CharField(default='', max_length=14),
        ),
    ]