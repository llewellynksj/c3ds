from django.db import models
from cloudinary.models import CloudinaryField


class Carousel(models.Model):
    hero_image = CloudinaryField('image', default='hero_placeholder')
    tagline_text = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(
        help_text='Enter 1, 2, or 3', unique=True, default=1)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.tagline_text


class LatestNewsCard(models.Model):
    card_image = CloudinaryField('image', default='card_placeholder')
    title = models.CharField(max_length=30, unique=True)
    date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True, max_length=250)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class LatestResearchCard(models.Model):
    card_image = CloudinaryField('image', default='card_placeholder')
    title = models.CharField(max_length=30, unique=True)
    date = models.DateField(null=True, blank=True)
    summary = models.TextField(blank=True, max_length=250)
    url = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
