# Generated by Django 3.2.20 on 2023-10-17 07:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_alter_publication_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]