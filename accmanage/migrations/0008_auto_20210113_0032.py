# Generated by Django 3.1.5 on 2021-01-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accmanage', '0007_auto_20210113_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='creditcard_ED',
            field=models.DateTimeField(),
        ),
    ]