# Generated by Django 3.1.5 on 2021-01-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roommanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='currenthotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=15, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='room',
            old_name='AC',
            new_name='breakfast',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='MB',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='room',
            name='MW',
        ),
        migrations.RemoveField(
            model_name='room',
            name='TV',
        ),
        migrations.RemoveField(
            model_name='room',
            name='bath',
        ),
        migrations.RemoveField(
            model_name='room',
            name='kettle',
        ),
        migrations.RemoveField(
            model_name='room',
            name='kitchen',
        ),
        migrations.RemoveField(
            model_name='room',
            name='wifi',
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.CharField(default='', max_length=500, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='show',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='img',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='Room_Img',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('One Bed', 'One Bed'), ('Two Beds', 'Two Beds'), ('Three Beds', 'Three Beds')], default='One Bed', max_length=50),
        ),
    ]
