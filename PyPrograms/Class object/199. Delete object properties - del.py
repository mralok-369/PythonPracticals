class Student:
    def __init__(self,name,course,sex):
        self.name = name
        self.course = course
        self.sex = sex

    def show(self):
        print("Student Details : ")
        print("Name : ",self.name)
        print("Course : ",self.course)
        # print("Sex : ",self.sex)

s = Student("Mohit","M.tech","male")
s.show()

# deleting sex
del s.sex
s.show()



