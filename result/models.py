from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class AbstractSlug(models.Model):
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

class Subject(AbstractSlug):
    ''

class Teacher(AbstractSlug):
    marks_file = models.FileField(upload_to='marks', default='marks.csv')
    subject = models.OneToOneField(Subject, related_name='teacher', on_delete = models.CASCADE)

class Student(AbstractSlug):
    image  = models.ImageField(upload_to='profile-pic-student', default='default.png')
    rollno = models.CharField(max_length=50)
    teachers = models.ManyToManyField(Teacher, related_name='students')
    subjects = models.ManyToManyField(Subject, related_name ='substudents')



