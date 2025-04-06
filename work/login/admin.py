from django.contrib import admin
from .models import User_Status

class User_StatusAdmin(admin.ModelAdmin):
    list_filter = ('Isverified', 'is_staff')
admin.site.register(User_Status, User_StatusAdmin)