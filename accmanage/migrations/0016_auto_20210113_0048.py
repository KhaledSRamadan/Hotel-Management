# Generated by Django 3.1.5 on 2021-01-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0015_auto_20210113_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='creditcard_ED',
            field=models.CharField(default='ex: 03/24', max_length=5),
        ),
    ]