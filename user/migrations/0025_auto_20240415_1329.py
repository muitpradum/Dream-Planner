# Generated by Django 3.2.4 on 2024-04-15 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_requstprice_no_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imgallerys',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vigallerys',
            name='category',
        ),
    ]
