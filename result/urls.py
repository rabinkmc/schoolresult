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
        
        path('student/delete/<int:pk>-<str:slug>', views.StudentDeleteView.as_view(),name='student-delete'), 
        path('subject/delete/<int:pk>-<str:slug>', views.SubjectDeleteView.as_view(),name='subject-delete'), 
        path('teacher/delete/<int:pk>-<str:slug>', views.TeacherDeleteView.as_view(),name='teacher-delete'), 

        path('result/<int:pk>-<str:slug>/', views.result, name='result'), 
] 
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
