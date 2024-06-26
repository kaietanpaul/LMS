# Generated by Django 4.1.7 on 2023-03-07 11:30
from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(apps, schema_editor):
    User = get_user_model()

    User.objects.create_superuser(
        email='admin@admin.pl',
        fullname='Test Admin',
        password='testPass123'
    )


def delete_superuser(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_initial_groups'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser),
    ]
