# Generated by Django 3.2.20 on 2023-09-29 13:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_carousel_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_image', cloudinary.models.CloudinaryField(default='card_placeholder', max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, max_length=500)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.DeleteModel(
            name='OverviewCard',
        ),
    ]
