from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    CATEGORY = [
        ('Centre Director', 'Centre Director'),
        ('Research Fellow', 'Research Fellow'),
        ('Visiting Fellow', 'Visiting Fellow'),
    ]

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
    discipline = models.CharField(
        max_length=100)
    web_link = models.TextField(
        max_length=2000,
        default='www.google.com',
        help_text="Please enter full web address including 'https://'")
    summary = models.TextField(
        max_length=2000)

    def __str__(self):
        return self.name
