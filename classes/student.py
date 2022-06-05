import csv
import os.path
from classes.person import Person

class Student(Person):

    # def __init__(self, name, age, password, role, school_id):
    #     super().__init__(name, age, password, role)
    #     self.school_id = school_id

    # @classmethod
    # def objects(cls):
    #     students = []
    #     my_path = os.path.abspath(os.path.dirname(__file__))
    #     path = os.path.join(my_path, "../data/students.csv")
    #     with open(path) as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             students.append(Student(**dict(row)))
    #     return students

    student_list = []

    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def objects(cls):
        file_name = './data/students.csv'
        

        with open(file_name, newline='') as student_file:
            reader = csv.DictReader(student_file)

            for row in reader:
                cls.student_list.append(row)

        return cls.student_list

    @classmethod
    def add_student(cls, name, age, role, school_id, password):
        cls.student_list.append({'name': name, 'age': age, 'role': role, 'school_id': school_id, 'password': password})

    @classmethod
    def remove_student(cls, school_id):
        for i,item in enumerate(Student.student_list):
            if school_id == item['school_id']:
                Student.student_list.pop(i)

    def __str__(self):
        return (f'{self.name}\n********\nage: {self.age}\nid: {self.school_id}')
