from django.contrib import admin
from .models import *


# Register your models here.

class MytableAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['year']
    list_display = ("id", "title", "author", "editor", "year")

admin.site.register(Mytable,MytableAdmin)

#@admin.register(Mytable)
#class Mytable(admin.ModelAdmin):
#    list_dispay = {'rno', 'title', 'author', 'editor', 'year')

