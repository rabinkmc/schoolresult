from django.urls import path, include
from rest_framework.routers import DefaultRouter

from result import views 
router = DefaultRouter()

router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'subjects', views.SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('result/<int:pk>',views.Result.as_view(), name='result')
]
