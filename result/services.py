import csv
import os
from result.models import Student, Teacher, Subject
from core.settings import MEDIA_ROOT

marks_path  = os.path.join(MEDIA_ROOT ,'marks.csv')
students_name_path  = os.path.join(MEDIA_ROOT ,'student.csv')

def get_student_and_rollnumber(filepath=students_name_path):
    students_name_with_rollno = {}
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            rollno = row['rollno']
            students_name_with_rollno[name] = rollno
    return students_name_with_rollno

def get_marks_and_roll_number(filepath=marks_path):
    markslist_with_rollno = {}
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            rollno = row['rollno'] 
            marks = row['marks']
            markslist_with_rollno[rollno] = marks
    return markslist_with_rollno

teachersList = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa', 'Rakesh Mahat']
teachers = [ {'name': teacher } for teacher in teachersList] 

subjects = [{'name':'maths'},
            {'name':'nepali'},
            {'name':'english'}, 
            {'name':'science'}, 
            {'name':'social'}
            ] 

def load_subjects_in_Subject():
    for subject in subjects:
        Subject.objects.create(**subject)

def load_teachers_in_Teacher():
    for teacher,subject in zip(teachers,Subject.objects.all()):
        Teacher.objects.create(**teacher, subject=subject)

def load_students_in_Student(students_name_with_rollno):
    for student in students_name_with_rollno:
        Student.objects.create(**student)

def set_marks_in_Student(subject, marks_file_path=marks_path):
    marks_from_rollno = get_marks_and_roll_number(marks_file_path)
    for student in Student.objects.all():
        rollno = student.rollno
        marks = round(float(marks_from_rollno.get(rollno)),2)
        setattr(student,subject,marks)
        student.save()




