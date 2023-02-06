class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def show(self):
        print("Student Details : ")
        print("Name : ",self.name)
        print("Course : ",self.course)

s1 = Student("Mohit","M.tech")
s2 = Student("Vinita","B.E.")

s1.show()
s2.show()

del s2

s1.show()
# s2.show()


