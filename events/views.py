from django.shortcuts import render
from .models import NewsCard


def display_events(request):
    """
    Display the events page
    """
    return render(request, 'events.html', {})


def display_news(request):
    """
    Display the news page
    """
    news_card_objects = NewsCard.objects.all
    return render(
        request,
        'news.html',
        {'news_card_objects': news_card_objects})
