# Generated by Django 4.0.4 on 2022-05-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptpet',
            name='address',
        ),
        migrations.RemoveField(
            model_name='foundedpet',
            name='address',
        ),
        migrations.RemoveField(
            model_name='lostpet',
            name='address',
        ),
        migrations.AddField(
            model_name='adoptpet',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='foundedpet',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lostpet',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
    ]