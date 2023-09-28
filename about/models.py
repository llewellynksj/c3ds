from django.db import models
from django.core.validators import EmailValidator


class Enquiry(models.Model):
    """
    Enquiry model saves contact form submissions
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator])
    message = models.TextField(max_length=800)

    def __str__(self):
        return self.full_name
