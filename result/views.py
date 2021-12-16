from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.views.generic import DetailView,ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.db.models import Sum,Count,Avg,Min,Max
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, Avg
from django.http import HttpResponse 

from result.models import Student, Teacher, Subject,Mark, TestModel
from result.serializers import (StudentSerializer, TeacherSerializer,
SubjectSerializer, MarkSerializer, ResultSerializer, TestModelSerializer )

from result.forms import StudentForm,TeacherForm, SubjectForm
from result.readcsv import read_csv
from rest_framework.reverse import reverse
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'students': reverse('api-student-list', request=request, format=format),
        'teachers': reverse('api-teacher-list', request=request, format=format), 
        'subjects': reverse('api-subject-list', request=request, format=format)
    })

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

class TestDetail(APIView):
    def get(self, request):
        tests = TestModel.objects.all()
        serializer = TestModelSerializer(tests,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TestModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestModelSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
