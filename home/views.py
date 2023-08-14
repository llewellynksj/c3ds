from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def people(request):
    return render(request, 'people.html', {})


def about(request):
    return render(request, 'about.html', {})


def partners(request):
    return render(request, 'partners.html', {})
