import csv

def get_marks_and_roll_number(filepath):
    markslist_with_roll_no = []
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            info = {
                    'rollno': row['rollno'],
                    'marks': row['marks'],
                    }
            markslist.append(info)
    return markslist_with_roll_no

def get_student_and_rollnumber(filepath):
    students_name_with_rollno = []
    with open(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f)
        for row in reader:
            info = { 'name': row['name'],
                    'rollno': row['rollno'],
                    }
            students_name_with_rollno.append(info)
    return students_name_with_rollno


teachers = ['Doleshwor Niraula', 'Santosh Bhattarai', 'Prem Thapa','Nirajan Thapa']

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
    for subject in Subject.objects.all():
        Teacher.objects.create(**teacher, subject=subject)

def load_students_in_Student(students_name_with_rollno):
    for student in students_name_with_rollno:
        Student.objects.create(**student)


set_marks_in_Student(subject, marks_from_roll_number):
    for student in Student.objects.all():
        setattr(student,subject, marks_from_roll_number[student.rollno])




