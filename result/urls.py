from django.urls import path

from result.views import ( home, StudentListView, StudentDetailView,
        TeacherListView,TeacherDetailView)

urlpatterns = [  
        path('', home, name='home'), 
        path('student/', StudentListView.as_view(),name='student-list'), 
        path('teacher/', TeacherListView.as_view(),name='teacher-list'), 
        path('student/<int:pk>-<str:slug>/',StudentDetailView.as_view(),name='student-pk-slug-detail'), 
        path('teacher/<int:pk>-<str:slug>/',TeacherDetailView.as_view(),name='teacher-pk-slug-detail'), 
]


