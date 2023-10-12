from django.db import models
from django.core.validators import EmailValidator


class ContactDetail(models.Model):
    """
    ContactDetail model allows admin to add and
    update address and email address
    """
    first_line_of_address = models.CharField(
        max_length=200)
    second_line_address = models.CharField(
        max_length=200,
        default='Enter second line of address')
    city = models.CharField(
        max_length=50)
    county = models.CharField(
        max_length=50)
    postcode = models.CharField(
        max_length=15)
    email = models.EmailField(
        validators=[EmailValidator])
