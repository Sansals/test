from django.contrib import admin
from .models import Articles, Public_Chat, ForumQuestions, ForumAnswer

admin.site.register(Articles)
admin.site.register(Public_Chat)
admin.site.register(ForumQuestions)
admin.site.register(ForumAnswer)
# Register your models here.
