import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from result.models import Student, Teacher, Subject, Mark
from result.serializers import (StudentSerializer, TeacherSerializer,
ResultSerializer, MarkSerializer, SubjectSerializer)

client = Client()

class GetModelsTest(TestCase):
    ''''''
    def SetUp(self):
        maths = Subject.objects.create(name='maths')
        social = Subject.objects.create(name='social')
        rabin = Student.objects.create(name='Rabin Dhamala', rollno='073BEL329')
        abin = Student.objects.create(name='Abin Nakarmi', rollno='073BEL329')
        dn_sir  = Teacher.objects.create(name='DN sir') 
        santosh_sir = Teacher.objects.create(name='Santosh sir') 

    def test_get_teachers(self):
        serializer = TeacherSerializer(Teacher.objects.all(), many=True)
        response = client.get(reverse('api-teacher-list'))
        self.assertEqual(response.data.get('result'), serializer.data)
