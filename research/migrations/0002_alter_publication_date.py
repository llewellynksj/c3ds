# Generated by Django 3.2.20 on 2023-09-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(help_text='Please enter MM/DD/YYYY'),
        ),
    ]
