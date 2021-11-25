from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from result.views import ( home, 
        StudentListView, StudentDetailView, StudentCreateView, StudentDeleteView,StudentUpdateView,
        TeacherListView,TeacherDetailView, TeacherCreateView, TeacherDeleteView,TeacherUpdateView,
        SubjectListView,SubjectDetailView, SubjectCreateView, SubjectDeleteView,SubjectUpdateView,
        )

urlpatterns = [  
        path('', home, name='home'), 

        path('student/', StudentListView.as_view(),name='student-list'), 
        path('subject/', SubjectListView.as_view(),name='subject-list'), 
        path('teacher/', TeacherListView.as_view(),name='teacher-list'), 

        path('student/<int:pk>-<str:slug>/',StudentDetailView.as_view(),name='student-pk-slug-detail'), 
        path('subject/<int:pk>-<str:slug>/',SubjectDetailView.as_view(),name='subject-pk-slug-detail'), 
        path('teacher/<int:pk>-<str:slug>/',TeacherDetailView.as_view(),name='teacher-pk-slug-detail'), 
    
        path('student/create/', StudentCreateView.as_view(),name='student-create'), 
        path('subject/create/', SubjectCreateView.as_view(),name='subject-create'), 
        path('teacher/create/', TeacherCreateView.as_view(),name='teacher-create'), 

        path('student/update/<int:pk>-<str:slug>/', StudentUpdateView.as_view(),name='student-update'), 
        path('subject/update/<int:pk>-<str:slug>/', SubjectUpdateView.as_view(),name='subject-update'), 
        path('teacher/update/<int:pk>-<str:slug>/', TeacherUpdateView.as_view(),name='teacher-update'), 
        
        path('student/delete/<int:pk>-<str:slug>', StudentDeleteView.as_view(),name='student-delete'), 
        path('subject/delete/<int:pk>-<str:slug>', SubjectDeleteView.as_view(),name='subject-delete'), 
        path('teacher/delete/<int:pk>-<str:slug>', TeacherDeleteView.as_view(),name='teacher-delete'), 

] 

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
