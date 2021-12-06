from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.views.generic import DetailView,ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.db.models import Sum,Count,Avg,Min,Max
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, Avg
from django.http import HttpResponse 

from result.models import Student, Teacher, Subject,Mark
from result.serializers import StudentSerializer, TeacherSerializer, SubjectSerializer, MarkSerializer, ResultSerializer

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

    # def get_success_url(self):
    #     self.object.get_records()
    #     return super().get_success_url(self)

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

class MarkCreateView(CreateView):
    model = Mark
    fields =['subject', 'student', 'marks']
    template_name = 'result/student_form.html'


class MarkUpdateView(UpdateView):
    model = Mark
    fields =['subject', 'student', 'marks']
    template_name = 'result/student_form.html'

    success_url = reverse_lazy('student-list')

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    
class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class Result(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = ResultSerializer(student)
        return Response(serializer.data)

def updatemarks(request, **kwargs):
    '''
    This view will be associated with teacher.

    ideally i would want this to be a post save or save method , as soon
    as teacher uploads the file, i want the marks to be changed. For
    now, i will create a button.
    '''

    teacher =get_object_or_404(Teacher, pk=6)
    return HttpResponse(f'<h1>{teacher}</h1>')



def result(request, *args, **kwargs):
    student = Student.objects.get(**kwargs)
    context = {}
    context['student'] = student
    context['subjects'] = student.mark_set.all()
    context['marks'] = student.mark_set.aggregate(marks = Sum('marks')).get('marks')
    context['percentage'] = round(student.mark_set.aggregate(total =Avg('marks')).get('total'),2)

    return render(request, 'result/result.html', context)

