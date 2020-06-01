from django.contrib import admin
from .models import Apartments


class ApartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'price', 'is_published')
    list_display_links = ('id', 'title', 'city', 'price')
    list_editable = ('is_published',)
    list_per_page = 30
    search_fields = ('title', 'price', 'description')

admin.site.register(Apartments, ApartmentsAdmin)
