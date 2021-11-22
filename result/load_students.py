from resultcli.read_marks import RecordList

from result.models import Student

def create_student():
    Student.objects.bulk_create(RecordList)
