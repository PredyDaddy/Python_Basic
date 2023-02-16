class Student:
    """A class to represent a University student"""
    # Add code here ...
    def __init__(self,firstname,lastname,course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course
        self.modulecode = []
    def showDetails(self):
        print(self.firstname,self.lastname,'on course:',self.course)
        print('Enrolled on following modules:')
        for i in self.modulecode:
            print(i)
    def changeCourse(self,newcourse):
        for i in self.course:
            i = newcourse
        
class Module:
    """A class to represent a single module"""
     # Add code here ...
    def __init__(self,name,code,tutor):
        self.name = name 
        self.code = code
        self.tutor = tutor
        self.enrolled_students = []
    def enrolStudent(self,student:Student):
        fullname = student.firstname +' '+student.lastname
        self.enrolled_students.append(fullname)
        student.modulecode.append(self.code)
    def showAllEnrolledStudents(self):
        if len(self.enrolled_students):
            print('Enrolled on module:',self.code)
            for i in self.enrolled_students:
                print(i)
        else:
            print('No students for',self.code,'yet')
    
        

   

def main():

    # Create some students and some modules ...
    s1 = Student('ken','barlow','english')
    s2 = Student('mike','baldwin','business')
    s3 = Student('harold','legg', 'medicine')

    m1 = Module('English language and semantics', 'A101','Wanda Pickle')
    m2 = Module('Engineering principles','E102','Buzz Jones')
    m3 = Module('Anatomy','M105','Greg House')

    # Now enrol some students on some modules ...
    m1.enrolStudent(s1)
    m1.enrolStudent(s2)
    m2.enrolStudent(s1)
    m2.enrolStudent(s3)

    # Have a look at some students and some modules ...
    s1.showDetails()
    s2.showDetails()
    s3.showDetails()

    m1.showAllEnrolledStudents()
    m2.showAllEnrolledStudents()
    m3.showAllEnrolledStudents()

    # Change a course ...
    s1.changeCourse('engineering')
    s1.showDetails()


if __name__ == "__main__":
    main()
