# Generated by Django 3.2.4 on 2024-04-11 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20240411_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scategory',
            old_name='speaker_name',
            new_name='event_place',
        ),
    ]
