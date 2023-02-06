class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def show(self):
        print("Student Details : ")
        print("Name : ",self.name)
        print("Course : ",self.course)

s = Student("Mohit","M.tech")
s.show()

s.course = "MBBS"
print("\nAfter modifying details \n")
s.show()