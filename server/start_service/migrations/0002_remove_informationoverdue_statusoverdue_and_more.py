# Generated by Django 4.2 on 2024-01-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationoverdue',
            name='StatusOverdue',
        ),
        migrations.AlterField(
            model_name='informationoverdue',
            name='Sum',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='informationoverdue',
            name='Type',
            field=models.IntegerField(),
        ),
    ]