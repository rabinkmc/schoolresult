from django.urls import path

from result import views 

urlpatterns = [  
        path('', views.api_root, name='api-root'), 

        path('api/v1/student/',  views.StudentListCreate.as_view(),name='api-student-list'), 
        path('api/v1/subject/',  views.SubjectList.as_view(),name='api-subject-list'), 
        path('api/v1/teacher/',  views.TeacherList.as_view(),name='api-teacher-list'), 

        path('api/v1/student/<int:pk>/', views.StudentDetail.as_view(), name='api-student-detail'), 
        path('api/v1/subject/<int:pk>/', views.SubjectDetail.as_view(), name='api-subject-detail'), 
        path('api/v1/teacher/<int:pk>/', views.TeacherDetail.as_view(), name='api-teacher-detail'), 

        path('api/v1/result/<int:pk>/', views.Result.as_view(), name='api-result'),
        path('api/v1/test/', views.TestDetail.as_view(), name='api-test'),

] 

