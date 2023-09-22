from django.shortcuts import render, get_object_or_404


def display_projects(request):
    """
    Displays the Current Projects page
    """
    return render(request, 'projects.html', {})


def display_publications(request):
    """
    Displays the Publications page
    """
    return render(request, 'publications.html', {})
