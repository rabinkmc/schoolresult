# Generated by Django 3.2.9 on 2021-11-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20211124_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='marks_file',
            field=models.FileField(default='marks.csv', upload_to='csv/'),
        ),
    ]
