# Generated by Django 3.2.20 on 2023-09-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_profile_web_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='job_category',
            field=models.CharField(choices=[('Centre Director', 'Centre Director'), ('Researchers', 'Researchers')], default='Centre Director', max_length=100),
        ),
    ]
