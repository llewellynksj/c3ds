# Generated by Django 3.2.20 on 2023-08-21 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_carousel_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['order']},
        ),
    ]
