from django.contrib import admin
from .models import Publication
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Publication)
class PublicationAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
