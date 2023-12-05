class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        #composition
        self.classrooms = {}
        self.teachers = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom] = classroom
    
    def add_teachers(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def student_addmission(self, student):
        classname = student.classroom.name
        if classname in self.classrooms:
            self.classrooms[ classname].add_student(student)
        else:
            print(f'{classname} is not exist in this school')
    
    def __repr__(self) -> str:
        for key, val in self.classrooms.items():
            print(key, val)
        return ''

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        #composition
        self.students = []
        self.subjects = []

    def add_student(self, student):
        student_id = f'{self.name}-{len(self.students)+1}'
        student.id = student_id
        self.students.append(student)
    
    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    #top student according to their grade
    def top_student(self):
        pass