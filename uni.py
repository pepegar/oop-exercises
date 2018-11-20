#%%

class Student:
    
    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
        
    def apply(self, university):
        if university.accepts(self):
            return True
        else:
            return False
        
        
class University:

    def __init__(self, min_GPA, courses_list):
        self.min_GPA = min_GPA
        self.courses_list = courses_list
        
    def accepts(self, student):
        if student.GPA >= self.min_GPA:
            return True
        else:
            return False
        
class Course:
    
    students = []
    
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students

    
    def enroll_student(self, student):
        print(student.name + " is trying to enroll in " + self.name)
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("bad luck fella")
    
    
tax_evasion = Course("tax evasion 101", 100)
courses_delaware = [tax_evasion]
delaware_uni = University(1.3, courses_delaware)
    
pepe = Student("Pepe", 1.3)

persuasion = Course("presentation skills", 27)
programming = Course("programming", 1)
courses_ie = [
        persuasion,
        programming
        ]
ie_uni = University(3.6, courses_ie)

anthony = Student("anthony", 4)

programming.enroll_student(pepe)
programming.enroll_student(anthony)
for student in programming.students:
    print(student.name + " is enrolled in programming")






    
    
    