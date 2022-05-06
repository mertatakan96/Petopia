# Generated by Django 4.0.4 on 2022-05-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_business',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_petlover',
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(editable=False, max_length=20, null=True),
        ),
    ]
