from django.shortcuts import render
from .models import ContactDetail


def display_contact(request):
    """
    Displays the contact page
    """
    details_list = ContactDetail.objects.all()

    return render(
        request, 'contact.html', {'details_list': details_list})


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
