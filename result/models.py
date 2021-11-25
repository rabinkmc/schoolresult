from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class AbstractNameSlug(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(
            default='',
            editable=False,
            max_length=100
            )

    class Meta:
        abstract = True

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
    marks_file = models.FileField(upload_to='csv/', default='marks.csv')
    subject = models.OneToOneField(Subject, related_name='teacher', on_delete = models.CASCADE)

class Student(AbstractNameSlug):
    image  = models.ImageField(upload_to='profile-pic-student', default='default.png')
    rollno = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher, related_name='students')
    # subjects = models.ManyToManyField(Subject, related_name ='substudents', through='Marks')
    subjects = models.ManyToManyField(Subject, related_name ='substudents')
    english = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    maths =   models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    nepali =  models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    social =  models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    science = models.DecimalField(null=True, blank=True,max_digits=5, decimal_places=2)
    result = models.ForeignKey('Result', on_delete=models.CASCADE, blank=True,null=True)

# class Marks(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sub_marks')
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='std_marks')
#     marks = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    
# class Result(models.Model):
#     total = models.DecimalField(null=True, blank=True)


