# Generated by Django 3.1.5 on 2021-01-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20210116_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='weekend',
        ),
        migrations.AddField(
            model_name='route_details',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
