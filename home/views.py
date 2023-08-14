from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Carousel, OverviewCard


def home(request):
    carousel_objects = Carousel.objects.all
    overview_card_objects = OverviewCard.objects.all
    context = {'carousel_objects': carousel_objects, 'overview_card_objects': overview_card_objects}
    return render(request, 'home.html', context)


def people(request):
    return render(request, 'people.html', {})


def about(request):
    return render(request, 'about.html', {})


def partners(request):
    return render(request, 'partners.html', {})
