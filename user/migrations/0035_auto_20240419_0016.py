# Generated by Django 3.2.4 on 2024-04-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_auto_20240417_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo',
            name='screenshots',
        ),
        migrations.AddField(
            model_name='ngo',
            name='utr',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
