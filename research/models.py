from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class Publication(models.Model):
    """
    Model to hold database of information for publications
    """
    title = models.TextField(max_length=2000)
    thumbnail = CloudinaryField('image', default='publication_placeholder')
    date = models.DateField(help_text='Please enter MM/DD/YYYY')
    type = models.CharField(max_length=255)
    publication = models.CharField(max_length=255)
    authors = models.TextField(max_length=2000)
    description = HTMLField(
        blank=True,
        null=True,)
    url = models.URLField()

    class Meta:
        """
        Metadata Class Container
        """
        ordering = ['-date']

    def __str__(self):
        """
        Function that returns main publication objects as a string
        """
        return f'{self.publication} - "{self.title}"'
