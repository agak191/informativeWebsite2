# Generated by Django 3.2.8 on 2021-10-27 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informativeApp', '0002_rename_venue_usersurvey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersurvey',
            name='owner',
        ),
    ]
