from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
import datetime
from datetime import datetime


class Profile(models.Model):
    CATEGORY = [
        ('Centre Director', 'Centre Director'),
        ('Researchers', 'Researchers'),
    ]
    created_on = models.DateTimeField(default=timezone.now())
    profile_pic = CloudinaryField(
        'image',
        default='profile_pic_placeholder')
    name = models.CharField(
        max_length=100)
    job_category = models.CharField(
        max_length=100,
        choices=CATEGORY,
        default='Centre Director')
    job_title = models.CharField(
        max_length=500)
    summary = models.TextField(
        max_length=10000)
    expertise = models.CharField(
        max_length=500,
        blank=True,
        null=True,)
    web_link = models.TextField(
        max_length=2000,
        default='www.google.com',
        help_text="Please enter full web address including 'https://'")

    def __str__(self):
        return self.name
