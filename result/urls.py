from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from result import views 

list_actions = {
    'get': 'list',
    'post': 'create'
}

detail_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

student_list = views.StudentViewSet.as_view(list_actions)
student_detail = views.StudentViewSet.as_view(detail_actions)
teacher_list =views.TeacherViewSet.as_view(list_actions)
teacher_detail = views.TeacherViewSet.as_view(detail_actions)
subject_list= views.SubjectViewSet.as_view(list_actions)
subject_detail= views.SubjectViewSet.as_view(detail_actions)

urlpatterns = format_suffix_patterns([  
        path('', views.api_root, name='api-root'), 

        path('api/v1/student/',student_list, name='api-student-list'), 
        path('api/v1/student/<int:pk>', student_detail, name='api-student-detail'), 

        path('api/v1/teacher/',teacher_list, name='api-teacher-list'), 
        path('api/v1/teacher/<int:pk>',teacher_list, name='api-teacher-list'), 

        path('api/v1/subject/',subject_list, name='api-subject-list'), 
        path('api/v1/subject/<int:pk>',subject_list, name='api-subject-list'), 

        path('api/v1/result/<int:pk>/', views.Result.as_view(), name='api-result'),
        path('api/v1/test/', views.TestDetail.as_view(), name='api-test'),
]) 

