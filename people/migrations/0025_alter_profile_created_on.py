# Generated by Django 3.2.20 on 2023-10-12 12:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0024_alter_profile_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 12, 12, 1, 20, 124547, tzinfo=utc)),
        ),
    ]
