# Generated by Django 3.2.25 on 2024-12-22 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profiles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Sity',
        ),
    ]