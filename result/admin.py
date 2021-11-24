from django.contrib import admin

from result.models import Student, Teacher
admin.site.register([Student,Teacher])
