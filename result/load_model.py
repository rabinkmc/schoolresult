from result.models import Student, Teacher, Subject, Mark
from result.readcsv import read_csv
import os
from core.settings import MEDIA_ROOT

student_file  = os.path.join(MEDIA_ROOT ,'student.csv')
subjects_name = ['english','maths','nepali','science','social']
teachers_name = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa', 'Rakesh Mahat']


def load_subjects( subjects=subjects_name ):
    for subject in subjects:
        Subject.objects.create(name = subject)

def load_teachers( teachers=teachers_name ):
    for teacher,subject in zip(teachers,Subject.objects.all()):
        Teacher.objects.create(name=teacher, subject=subject)

def load_students( students = read_csv(student_file) ):
    for name,rollno in students.items():
        Student.objects.create(name=name,rollno=rollno)

def load_models():
    load_subjects()
    load_teachers()
    load_students()
