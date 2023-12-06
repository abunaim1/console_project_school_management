from school import*
from persons import*
def main():
    #create school
    scl = School('Adam Gorgie', 'U TT RRX')

    #create classroom
    eight = ClassRoom('eight')
    nine = ClassRoom('nine')
    ten = ClassRoom('ten')

    scl.add_classroom(eight)
    scl.add_classroom(nine)
    scl.add_classroom(ten)

    #create student
    alex = Student('Alex Z', eight)
    scl.student_addmission(alex)
    rolex = Student('Vikram', eight)
    scl.student_addmission(rolex)
    john = Student('PK john', eight)
    scl.student_addmission(john)

    #create subject
    physics_teacher = Teacher('Tapan')
    physics = Subject('Physics', physics_teacher )
    eight.add_subject(physics) 

    chemistry_teacher = Teacher('Haradhon Nag')
    chemistry = Subject('Chemistry', chemistry_teacher )
    eight.add_subject(chemistry) 

    biology_teacher = Teacher('Gazi Azmal')
    biology = Subject('biology', biology_teacher )
    eight.add_subject(biology) 
    
    eight.take_semester_final()
    print(scl)

if __name__ == '__main__':
    main()