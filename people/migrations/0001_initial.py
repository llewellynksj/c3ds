# Generated by Django 3.2.20 on 2023-08-21 11:17

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', cloudinary.models.CloudinaryField(default='profile_pic_placeholder', max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=500)),
                ('discipline', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=2000)),
            ],
        ),
    ]
