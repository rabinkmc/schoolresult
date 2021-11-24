from result.models import Student, Teacher, Subject


def get_marks(filepath):
    markslist = []
    with file(filepath, "r", newline='') as f: 
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            info = {
                    'rollno': row['rollno'],
                    'marks': row['marks'],
                    }

            markslist.append(info)
    return markslist








