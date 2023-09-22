from django.urls import path
from . import views

urlpatterns = [
    path(
        'projects',
        views.display_projects,
        name='projects'),
    path(
        'publications',
        views.display_publications,
        name='publications'),
]
