from django.db import models
from cloudinary.models import CloudinaryField


class Carousel(models.Model):
    hero_image = CloudinaryField('image', default='hero_placeholder')
    tagline_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tagline_text


class OverviewCard(models.Model):
    card_image = CloudinaryField('image', default='card_placeholder')
    title = models.CharField(max_length=30, unique=True)
    summary = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title
