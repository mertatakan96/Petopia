# Generated by Django 4.0.4 on 2022-05-22 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcements', '0004_alter_adoptpet_options_alter_foundedpet_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostPetComment',
            fields=[
                ('body', models.TextField(max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('announce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='announcements.lostpet')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='FoundedPetComment',
            fields=[
                ('body', models.TextField(max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('announce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='announcements.foundedpet')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AdoptPetComment',
            fields=[
                ('body', models.TextField(max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('announce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='announcements.adoptpet')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
