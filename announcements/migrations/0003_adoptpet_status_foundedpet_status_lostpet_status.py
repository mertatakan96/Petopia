# Generated by Django 4.0.4 on 2022-05-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_remove_adoptpet_address_remove_foundedpet_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptpet',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='foundedpet',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lostpet',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=20, null=True),
        ),
    ]
