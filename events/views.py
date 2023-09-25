from django.shortcuts import render


def display_events(request):
    """
    Display the events page
    """
    return render(request, 'events.html', {})
