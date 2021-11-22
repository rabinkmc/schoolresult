# Generated by Django 3.2.9 on 2021-11-22 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.CharField(max_length=50)),
                ('english', models.DecimalField(decimal_places=2, max_digits=5)),
                ('maths', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nepali', models.DecimalField(decimal_places=2, max_digits=5)),
                ('science', models.DecimalField(decimal_places=2, max_digits=5)),
                ('social', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('slug', models.SlugField(default='', editable=False, max_length=100)),
            ],
        ),
    ]
