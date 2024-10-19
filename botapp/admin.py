from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'number', 'person', 'executor', 'status', 'tags']
    search_fields = ('person', 'tags')  # Поиск по номеру и тексту заявки
