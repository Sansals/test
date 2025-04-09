from django.contrib import admin
from .models import Articles, Public_Chat, ForumTechQuestions, ForumComplaints, ForumComplaintAnswer, ForumTechAnswer

admin.site.register(Articles)
admin.site.register(Public_Chat)
admin.site.register(ForumTechQuestions)
admin.site.register(ForumComplaints)
admin.site.register(ForumComplaintAnswer)
admin.site.register(ForumTechAnswer)
# Register your models here.
