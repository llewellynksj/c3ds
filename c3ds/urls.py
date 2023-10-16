from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('people/', include('people.urls')),
    path('research/', include('research.urls')),
    path('resources/', include('resources.urls')),
    path('events/', include('events.urls')),
]
