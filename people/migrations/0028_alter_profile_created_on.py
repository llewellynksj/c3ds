# Generated by Django 3.2.20 on 2023-10-16 13:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0027_alter_profile_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 16, 13, 37, 43, 106767, tzinfo=utc)),
        ),
    ]