from django.shortcuts import render
from django.views.generic import DetailView,ListView

from result.models import Student


def home(request):
    return render(request, 'result/home.html')

class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student
