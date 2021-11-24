from django.urls import path

from result.views import ( home, 
        StudentListView, StudentDetailView, StudentCreateView,
        TeacherListView,TeacherDetailView, TeacherCreateView,
        SubjectListView,SubjectDetailView, SubjectCreateView,
        )

urlpatterns = [  
        path('', home, name='home'), 
        path('student/', StudentListView.as_view(),name='student-list'), 
        path('subject/', TeacherListView.as_view(),name='subject-list'), 
        path('teacher/', TeacherListView.as_view(),name='teacher-list'), 
        path('student/create/', StudentCreateView.as_view(),name='student-create'), 
        path('subject/create/', SubjectCreateView.as_view(),name='subject-create'), 
        path('teacher/create/', TeacherCreateView.as_view(),name='teacher-create'), 
        path('student/<int:pk>-<str:slug>/',StudentDetailView.as_view(),name='student-pk-slug-detail'), 
        path('subject/<int:pk>-<str:slug>/',SubjectDetailView.as_view(),name='subject-pk-slug-detail'), 
        path('teacher/<int:pk>-<str:slug>/',TeacherDetailView.as_view(),name='teacher-pk-slug-detail'), 
]


