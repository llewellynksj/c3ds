from django.urls import path
from . import views

urlpatterns = [
    path(
        'about',
        views.display_about,
        name='about'),
    path(
        'partners',
        views.display_partners,
        name='partners'),
    path(
        'contact',
        views.display_contact,
        name='contact'),
]
