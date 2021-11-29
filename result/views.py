from django.shortcuts import render,redirect
from django.views.generic import DetailView,ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum,Count,Avg,Min,Max

from result.models import Student, Teacher, Subject
from result.forms import StudentForm,TeacherForm, SubjectForm
from result.readcsv import read_csv

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

    def form_valid(self,form):
        self.get_records()
        return super().form_valid(form)

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

    def form_valid(self,form):
        self.get_records()
        return super().form_valid(form)

def result(request, *args, **kwargs):
    student = Student.objects.get(**kwargs)

    context = {}
    context['object'] = student
    context['subjects'] = student.mark_set.all()
    context['marks'] = student.mark_set.aggregate(Sum('marks'))
    context['percentage'] = student.mark_set.aggregate(Avg('marks'))

    return render(request, 'result/result.html', context)

