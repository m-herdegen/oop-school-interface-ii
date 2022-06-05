from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def find_student_by_id(self, id):

        check = next((item for item in self.students if item['school_id'] == id), 'there is no student with that id')
        return check

        
    def list_students(self):
        for item in self.students:
            print(f"{item['name']} {item['school_id']}")