from result.models import Student, Teacher, Subject, Mark
from result.services import read_csv

import os
from core.settings import MEDIA_ROOT

marks_path  = os.path.join(MEDIA_ROOT ,'marks.csv')
student_file  = os.path.join(MEDIA_ROOT ,'student.csv')

subjects_name = ['english','maths','nepali','science','social']
def load_subjects( subjects=subjects_name ):
    for subject in subjects:
        Subject.objects.create(name = subject)

teachers_name = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa', 'Rakesh Mahat']
def load_teachers( teachers=teachers_name ):
    for teacher,subject in zip(teachers,Subject.objects.all()):
        Teacher.objects.create(name=teacher, subject=subject)

def load_students( students = read_csv(student_file) ):
    for name,rollno in students.items():
        Student.objects.create(name=name,rollno=rollno)

def set_marks( subject, marks = read_csv(marks_path) ):
    for roll,mark in marks.items():
        mark = round(float(mark),2)
        print('roll:::',Student.objects.first().rollno, roll)
        student = Student.objects.get(rollno=roll)
        setattr(student,subject,mark)
        student.save()

# def get_result(student):
#     try:
#         subs = [ student.english , student.nepali , student.science , student.social , student.maths ] 
#         fail = any(subject < 32 for subject in subs)
#         marks = sum(subs)
#         percentage = '*' if fail else marks/len(subs)

#     except:
#         marks = None
#         percentage = None

#     return (marks, percentage)
    
