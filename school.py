class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        #composition
        self.classrooms = {}
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    
    def student_addmission(self, student, class_name):
        if class_name in self.classrooms:
            self.classrooms[class_name].add_student(student)
        else:
            print(f'{class_name} is not exist in this school')

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        #composition
        self.students = []

    def add_student(self, student):
        student_id = f'{self.name}-{len(self.students)+1}'
        self.students.append(student)
    
    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    #top student according to their grade
    def top_student(self):
        pass