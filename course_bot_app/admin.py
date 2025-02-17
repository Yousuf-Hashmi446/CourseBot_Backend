from django.contrib import admin
from .models import Course, CourseContent, User

admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(User)
