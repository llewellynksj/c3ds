# Generated by Django 3.2.20 on 2023-10-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0006_alter_publication_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
