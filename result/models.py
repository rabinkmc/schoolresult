from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno  = models.CharField(max_length=50)
    english = models.DecimalField(max_digits=5, decimal_places=2)
    maths   = models.DecimalField(max_digits=5, decimal_places=2)
    nepali  = models.DecimalField(max_digits=5, decimal_places=2)
    science = models.DecimalField(max_digits=5, decimal_places=2)
    social  = models.DecimalField(max_digits=5, decimal_places=2)
    total   = models.DecimalField(max_digits=5, decimal_places=2)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    slug = models.SlugField(
            default='',
            editable=False,
            max_length=100
            )

    def get_absolute_url(self):
        kwargs = { 
                'pk': self.id, 
                'slug': self.slug
                }
        # cls = self.__class__.__name__.lower()

        return reverse(f'student-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

