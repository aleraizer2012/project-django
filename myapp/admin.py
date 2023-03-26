from django.contrib import admin
from .models import DocNumber

# Register your models here.
class DocNumberAdmin(admin.ModelAdmin):
    list_display = ('doctype', 'year', 'number')

admin.site.register(DocNumber, DocNumberAdmin)