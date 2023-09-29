from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Carousel, NewsCard


def Home(request):
    carousel_objects = Carousel.objects.all
    news_card_objects = NewsCard.objects.all
    context = {
        'carousel_objects': carousel_objects,
        'news_card_objects': news_card_objects}
    return render(request, 'home.html', context)


# def People(request):
#     return render(request, 'people.html', {})


def About(request):
    return render(request, 'about.html', {})


def Partners(request):
    return render(request, 'partners.html', {})
