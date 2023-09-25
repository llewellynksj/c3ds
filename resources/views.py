from django.shortcuts import render


def display_resources(request):
    """
    Displays resources page
    """
    return render(request, 'resources.html', {})
