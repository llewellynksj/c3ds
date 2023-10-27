from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.display_events,
        name='events'),
    path(
        'news',
        views.display_news,
        name='news'),
]
