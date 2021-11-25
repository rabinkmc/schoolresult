from django.forms import ModelForm
from result.models import Student, Subject, Teacher


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','marks_file','subject']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['image','name','rollno','teachers', 'subjects'] 

