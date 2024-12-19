from django.contrib import admin
from .models import MadLib

class MadLibAdmin(admin.ModelAdmin):
    list_display = ('title', 'template')

admin.site.register(MadLib, MadLibAdmin)
