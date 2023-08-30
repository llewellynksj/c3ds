from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayProfile.as_view(), name='people'),
]
