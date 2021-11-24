import csv 
import random
import os

from constants import STUDENT

subjects = [ "maths", "science", "social", "english", "nepali",] 

base_dir  = os.getcwd()
studentfile = os.path.join(base_dir, "marks", "_student.csv")

with open(studentfile, "w") as outfile:
    fieldnames = ['name','rollno']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for i,student in enumerate(STUDENT):
        writer.writerow({'name':student, 'rollno': f'073BEL{300+i}'})

for subject in subjects:
    file = subject + ".csv"
    filepath = os.path.join(base_dir, "marks", file)

    with open(filepath, "w") as outfile:
        fieldnames = ['name', subject]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for student in STUDENT:
            marks = random.randint(0,100)
            writer.writerow({'name':student, subject:marks})


