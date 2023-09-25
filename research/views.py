from django.shortcuts import render, get_object_or_404
from .models import Publication


def display_projects(request):
    """
    Displays the Current Projects page
    """
    return render(request, 'projects.html', {})


def display_publications(request):
    """
    Displays the Publications page
    """
    qs = Publication.objects.all()
    context = {
        'queryset': qs
    }
    return render(request, 'publications.html', context)
