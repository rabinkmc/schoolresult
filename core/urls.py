from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('result.urls')), 
    path('admin/', admin.site.urls),
]
