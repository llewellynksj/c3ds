from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('people/', views.people, name='people'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
]
