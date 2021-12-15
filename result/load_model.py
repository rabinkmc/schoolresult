from result.models import Student, Teacher, Subject, Mark
from result.readcsv import read_csv
import os
from core.settings import MEDIA_ROOT
from django.utils.text import slugify
from django.contrib.auth.models import User

student_file  = os.path.join(MEDIA_ROOT ,'student.csv')
subjects_name = ['english','maths','nepali','science','social']
teachers_name = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa', 'Rakesh Mahat']
teacher_pwd = ['541', '542', '543', '544', '545']

students_info = read_csv(student_file)

def load_subjects( subjects=subjects_name ):
    for subject in subjects:
        Subject.objects.create(name = subject)

def load_teachers( teachers=teachers_name ):
    subjects = Subject.objects.all()
    for teacher,pwd,subject in zip(teachers,teacher_pwd,subjects):
        user = User.objects.create_user(
                username=slugify(teacher),
                password=slugify(teacher+pwd)
                )
        Teacher.objects.create(user=user, name=teacher, subject=subject)

def load_students( students = read_csv(student_file) ):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    for name,rollno in students.items():
        user = User.objects.create_user(
                username=slugify(name),
                password=rollno
                )
        std = Student.objects.create(user=user, name=name,rollno=rollno)
        std.subjects.add(*subjects)
        std.teachers.add(*teachers)

    

def load_marks():
    for student in Student.objects.all():
        for subject in Subject.objects.all():
            Mark.objects.create(student=student, subject=subject)


def load_models():
    load_subjects()
    load_teachers()
    load_students()

    for student in Student.objects.all():
        for teacher in Teacher.objects.all():
            student.teachers.add(teacher)
            student.subjects.add(teacher.subject)

