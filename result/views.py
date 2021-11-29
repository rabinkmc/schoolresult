from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from result.models import Student, Teacher, Subject
from result.forms import StudentForm,TeacherForm, SubjectForm
from result.services import read_csv
from result.service2 import get_result, set_marks 

def home(request):
    return render(request, 'result/home.html')

class StudentListView(ListView):
    model = Student
    paginate_by = 10

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
    form_class = StudentForm

class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm

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
    form_class = StudentForm

class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm

def result(request, *args, **kwargs):
    student = Student.objects.get(**kwargs)
    context = {}
    context['object'] = student
    context['marks'],context['percentage'] = get_result(student)

    return render(request, 'result/result.html', context)

def loadmarks(request, *args, **kwargs): 
    teacher = Teacher.objects.get(*args,**kwargs)
    subject = teacher.subject.name
    marks  = teacher.marks_file.path
    marks = read_csv(marks)
    set_marks(subject,marks)
    return redirect(teacher)
