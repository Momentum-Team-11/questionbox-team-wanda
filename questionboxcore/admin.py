from django.contrib import admin
from api.models import Question, Answer
from django.contrib.auth.admin import UserAdmin, User



admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(User, UserAdmin)