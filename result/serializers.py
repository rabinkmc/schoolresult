from result.models import Student, Subject, Teacher, Mark
from rest_framework import serializers

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']

class TeacherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default='/media/default.png')
    marks_file = serializers.FileField(default='/media/marks.csv')

    class Meta:
        model = Teacher
        fields = ['pk', 'name', 'subject', 'marks_file','image']
        
class StudentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default='media/default.png')
    teachers = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
 
    class Meta:
        model = Student
        fields= ['name', 'rollno','teachers', 'subjects','image']

    def get_teachers(self, object):
        return object.teachers.all().values_list('name', flat=True)

    def get_subjects(self, object):
        return object.subjects.all().values_list('name', flat=True)


class MarkSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    student = StudentSerializer()
    class Meta:
        model = Mark
        fields = [ 'subject', 'student', 'marks' ] 


