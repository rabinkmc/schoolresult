from django.shortcuts import render
from django.views.generic import DetailView,ListView 
from django.views.generic.edit import CreateView

from result.models import Student, Teacher, Subject

def home(request):
    return render(request, 'result/home.html')

class StudentListView(ListView):
    model = Student

class SubjectListView(ListView):
    model = Subject

class TeacherListView(ListView):
    model = Teacher

class StudentDetailView(DetailView):
    model = Student

class TeacherDetailView(DetailView):
    model = Teacher

class SubjectDetailView(DetailView):
    model = Subject

class TeacherCreateView(DetailView):
    model = Teacher

class StudentCreateView(CreateView):
    model = Student
    fields = ['image','name','rollno','teachers', 'subjects'] 

class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name']

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name','marks_file','subject']

