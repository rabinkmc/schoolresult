from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from result import views 

urlpatterns = [  
        path('', views.home, name='home'), 

        path('student/', views.StudentListView.as_view(),name='student-list'), 
        path('subject/',  views.SubjectListView.as_view(),name='subject-list'), 
        path('teacher/',  views.TeacherListView.as_view(),name='teacher-list'), 

        path('student/<int:pk>-<str:slug>/', views.StudentDetailView.as_view(),name='student-pk-slug-detail'), 
        path('subject/<int:pk>-<str:slug>/',views.SubjectDetailView.as_view(),name='subject-pk-slug-detail'), 
        path('teacher/<int:pk>-<str:slug>/',views.TeacherDetailView.as_view(),name='teacher-pk-slug-detail'), 
    
        path('student/create/', views.StudentCreateView.as_view(),name='student-create'), 
        path('subject/create/', views.SubjectCreateView.as_view(),name='subject-create'), 
        path('teacher/create/', views.TeacherCreateView.as_view(),name='teacher-create'), 

        path('student/update/<int:pk>-<str:slug>/', views.StudentUpdateView.as_view(),name='student-update'), 
        path('subject/update/<int:pk>-<str:slug>/', views.SubjectUpdateView.as_view(),name='subject-update'), 
        path('teacher/update/<int:pk>-<str:slug>/', views.TeacherUpdateView.as_view(),name='teacher-update'), 
        path('teacher/loadmarks/<int:pk>-<str:slug>/',views.updatemarks,name='teacher-loadmarks'), 
        
        path('student/delete/<int:pk>-<str:slug>/', views.StudentDeleteView.as_view(),name='student-delete'), 
        path('subject/delete/<int:pk>-<str:slug>/', views.SubjectDeleteView.as_view(),name='subject-delete'), 
        path('teacher/delete/<int:pk>-<str:slug>/', views.TeacherDeleteView.as_view(),name='teacher-delete'), 

        path('result/<int:pk>-<str:slug>/', views.result, name='result'), 

        path('marks/create/', views.MarkCreateView.as_view(), name='add-marks'),
        path('marks/update/<int:pk>/', views.MarkUpdateView.as_view(), name='update-marks'),

        # drf 
        path('api/v1/student/',  views.StudentList.as_view(),name='api-student-list'), 
        path('api/v1/subject/',  views.SubjectList.as_view(),name='api-subject-list'), 
        path('api/v1/teacher/',  views.TeacherList.as_view(),name='api-teacher-list'), 

        path('api/v1/student/<int:pk>-<str:slug>/', views.StudentDetail.as_view(), name='api-student-detail'), 
        path('api/v1/subject/<int:pk>-<str:slug>/', views.SubjectDetail.as_view(), name='api-subject-detail'), 
        path('api/v1/teacher/<int:pk>-<str:slug>/', views.TeacherDetail.as_view(), name='api-teacher-detail'), 

        path('api/v1/result/<int:pk>/', views.Result.as_view(), name='api-result'),

] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
