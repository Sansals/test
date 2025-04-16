from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_filter = (['user'])
admin.site.register(News, NewsAdmin)

admin.site.register(Rules)
admin.site.register(News_Comments)

# Register your models here.
