from django.contrib import admin
from .models import Recipe, Search

admin.site.register(Recipe)
admin.site.register(Search)