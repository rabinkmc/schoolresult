from django.contrib import admin

from result.models import Student, Teacher, Subject
admin.site.register([Student,Subject, Teacher])
