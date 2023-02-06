class Employee:
    no_of_leave = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}"

harry = Employee("Harry Bhai",455,"instructor")
rohan = Employee("Rohan Das",4554,"Student")

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "instructure"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "student"

print(harry.name)
print(harry.printdetails())

print(rohan.name)
print(rohan.printdetails())
