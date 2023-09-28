from django.shortcuts import render, get_object_or_404


def display_contact(request):
    """
    Displays the contact page
    """
    return render(request, 'contact.html', {})


def display_about(request):
    """
    Displays the about page
    """
    return render(request, 'about.html', {})


def display_partners(request):
    """
    Displays the partners page
    """
    return render(request, 'partners.html', {})
