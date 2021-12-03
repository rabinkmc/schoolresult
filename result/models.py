from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from result.readcsv import read_csv

class AbstractNameSlug(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
            default='',
            editable=False,
            max_length=100
            )

    class Meta:
        abstract = True
        ordering = ['name']

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        cls = self.__class__.__name__.lower()

        return reverse(f'{cls}-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subject(AbstractNameSlug):
    ''

class Teacher(AbstractNameSlug):
    image  = models.ImageField(upload_to='profile-pic-teacher', default='default.png')
    marks_file = models.FileField(upload_to='csv/', default='marks.csv')
    subject = models.OneToOneField(Subject, related_name='teacher', on_delete = models.CASCADE)
    records = {}

    def get_records(self,*args,**kwargs):
        self.records = read_csv(self.marks_file.path)
        self.save()
        return self.records

class Student(AbstractNameSlug):
    image  = models.ImageField(upload_to='profile-pic-student', default='default.png')
    rollno = models.CharField(max_length=50, unique=True)
    teachers = models.ManyToManyField(Teacher, related_name='students')
    subjects = models.ManyToManyField(Subject, related_name ='substudents', through='Mark')

class Mark(models.Model):
     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)# related_name='sub_marks')
     student = models.ForeignKey(Student, on_delete=models.CASCADE)# related_name='std_marks')
     marks = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
     
     class Meta:
         unique_together=[['subject','student']]

     def save(self,*args,**kwargs):
         file_name= self.subject.teacher.marks_file.name
         if self.marks is None | file_name != 'marks.csv':
             records = self.subject.teacher.get_records()
             if self.marks is None | file_name is not 'marks.csv':
                 try:
                     self.marks = records.get(self.student.rollno)
                 except: 
                     self.marks = None

         super().save(*args,**kwargs)

     def __str__(self):
         return f"{self.student},{self.subject}:{self.marks}"
    
