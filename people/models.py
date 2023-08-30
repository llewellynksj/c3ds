from django.db import models
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    profile_pic = CloudinaryField('image', default='profile_pic_placeholder')
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=500)
    discipline = models.CharField(max_length=100)
    summary = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
