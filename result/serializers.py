from result.models import Student, Subject, Teacher, Mark

from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['rollno','teachers']
