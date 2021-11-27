import csv
import os
from result.models import Student, Teacher, Subject
from core.settings import MEDIA_ROOT

marks_path  = os.path.join(MEDIA_ROOT ,'marks.csv')
student_file  = os.path.join(MEDIA_ROOT ,'student.csv')

def read_csv(file):
    with open(file,"r",newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        filedict = {}
        key = fields[0]
        value = fields[1]
        for row in reader:
            filedict.update({ row[key]:row[value] } )

        return filedict
            
def get_student(filepath=student_file):
    students = []
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            rollno = row['rollno']
            info = { 'name': name, 'rollno':rollno } 
            students.append(info)
    return students

def get_marks(filepath=marks_path):
    marks = {}
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            rollno = row['rollno'] 
            marks = round(float(row['marks']),2)
            marks[rollno] = marks
    return marks

teachersList = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa', 'Rakesh Mahat']
teachers = [ {'name': teacher } for teacher in teachersList] 

subjects = [{'name':'maths'},
            {'name':'nepali'},
            {'name':'english'}, 
            {'name':'science'}, 
            {'name':'social'}
            ] 

def load_subjects():
    for subject in subjects:
        Subject.objects.create(**subject)

def load_teachers():
    for teacher,subject in zip(teachers,Subject.objects.all()):
        Teacher.objects.create(**teacher, subject=subject)

def load_students(students=get_student(student_file)):
    for student in students:
        Student.objects.create(**student)

def set_marks(subject, marks_file_path=marks_path):
    marks = get_marks(marks_file_path)
    for roll,mark in marks.items():
        student = Student.objects.get(rollno=roll)
        setattr(student,subject,mark)
        student.save()

#again this get_result is a function specific to model, but i also don't
# want to add extra methods to my model
# i can test this function independent of the model
def get_result(student):
    try:
        subs = [ student.english , student.nepali , student.science , student.social , student.maths ] 
        fail = any(subject < 32 for subject in subs)
        marks = sum(subs)
        percentage = '*' if fail else marks/len(subs)

    except:
        marks = None
        percentage = None

    return (marks, percentage)




    
    
