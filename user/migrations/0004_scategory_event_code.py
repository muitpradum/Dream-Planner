# Generated by Django 3.2.4 on 2024-04-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_booknow_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='scategory',
            name='event_code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
