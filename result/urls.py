from django.urls import path

from result.views import home, StudentListView, StudentDetailView

urlpatterns = [  
        path('', home, name='home'), 
        path('student/', StudentListView.as_view(),name='student-list'), 
        path('student/<int:pk>-<str:slug>/',StudentDetailView.as_view(),name='student-pk-slug-detail'), 
]


