from django.contrib import admin

from result.models import Student, Teacher, Subject,Mark
admin.site.register([Student,Subject, Teacher,Mark])
