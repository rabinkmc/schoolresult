from django.shortcuts import render
from django.views.generic import DetailView,ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

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

class StudentCreateView(CreateView):
    model = Student
    fields = ['image','name','rollno','teachers', 'subjects'] 

class SubjectCreateView(CreateView):
    model = Subject
    fields = ['name']

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['name','marks_file','subject']

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subject-list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teacher-list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name_suffix = '_update_form'
    fields = ['image','name','rollno','teachers', 'subjects'] 

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name_suffix = '_update_form'
    fields = ['name']

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name_suffix = '_update_form'
    fields = ['name','marks_file','subject']
