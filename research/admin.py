from django.contrib import admin
from .models import Publication
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Publication)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
