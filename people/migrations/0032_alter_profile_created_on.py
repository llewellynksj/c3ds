# Generated by Django 3.2.20 on 2023-10-18 09:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0031_auto_20231018_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 9, 40, 18, 976178, tzinfo=utc)),
        ),
    ]