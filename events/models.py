from django.db import models
from cloudinary.models import CloudinaryField


class NewsCard(models.Model):
    card_image = CloudinaryField(
        'image',
        default='card_placeholder',
        help_text='Please upload image with width 315px x height 200px')
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField(null=True, blank=True)
    short_summary = models.TextField(blank=True, max_length=500)
    long_summary = models.TextField(blank=True)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
