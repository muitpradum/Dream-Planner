# Generated by Django 3.2.4 on 2024-04-13 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20240413_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incategory',
            name='speaker_picture',
        ),
    ]
