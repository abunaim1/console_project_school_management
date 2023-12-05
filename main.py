from school import*
from persons import*
def main():
    #create school
    scl = School('Adam Gorgie', 'U TT RRX')

    #create classroom
    eight = ClassRoom('VIII')
    nine = ClassRoom('IX')
    ten = ClassRoom('X')

    scl.add_classroom(eight)
    scl.add_classroom(nine)
    scl.add_classroom(ten)

    #create student
    alex = Student('Alex X', eight)
    scl.student_addmission(alex)
    # print(scl)

if __name__ == '__main__':
    main()