from django.test import TestCase
import result.load_model 
from result.readcsv import read_csv
from result.load_model import load_subjects, load_teachers, load_students
from result.models import Student, Teacher, Subject

class ServicesTestCase(TestCase):
    def setUp(self):
        pass

    def test_can_read_csv_file(self):
        expected = {'Rabin Dhamala':'073BEL329'}
        output = read_csv('result/test.csv')
        self.assertEqual(output,expected)
    
    def test_models_are_loaded(self):
        subjects =['Nepali', 'Maths']
        load_subjects(subjects)
        self.assertEqual(Subject.objects.all().count(), len(subjects))

        teachers =['DN sir', 'NST']
        load_teachers(teachers)
        self.assertEqual(Teacher.objects.all().count(),
                len(teachers))
        
        students = { 'Rabin Dhamala': '073BEL329', 
                     'Abin Nakarmi': '073BEL301',
                }
        load_students(students)
        self.assertEqual(Student.objects.all().count(), len(students))
        
