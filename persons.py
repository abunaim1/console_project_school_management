import random
class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    def take_exam(self, subject, students):
        for student in students:
            mark = random.randint(0,100)

class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None

        self.mark = {}
        self.grade = None
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, student_id):
        self.__id = student_id