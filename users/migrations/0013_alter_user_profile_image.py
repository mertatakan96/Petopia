# Generated by Django 4.0.4 on 2022-05-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.jpg', null=True, upload_to='profiles/'),
        ),
    ]
