from result.models import Student, Subject, Teacher, Mark
from rest_framework import serializers
from django.db.models import Avg, Sum

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id','name']

class TeacherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default='/media/default.png')
    marks_file = serializers.FileField(default='/media/marks.csv')
    subject = serializers.StringRelatedField()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'subject', 'marks_file','image']
        
class StudentSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(default='media/default.png')
    teachers = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
 
    class Meta:
        model = Student
        fields= ['id','name', 'rollno','teachers', 'subjects','image']

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


class ResultSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id','name','subjects','percentage', 'total'] 

    def get_percentage(self,object):
        return object.mark_set.aggregate(percentage=Avg('marks'))
    
    def get_total(self,object):
        return object.mark_set.aggregate(total =Sum('marks'))
        
    def get_subjects(self, object):
        marksheet = object.mark_set.all()
        subject_marks = {}
        for mark in marksheet:
            subject_marks[mark.subject.name] = mark.marks
        return subject_marks
            
        

