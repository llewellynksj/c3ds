from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


class DisplayProfile(generic.ListView):
    """
    Displays profile page
    """
    model = Profile
    template_name = 'people.html'
