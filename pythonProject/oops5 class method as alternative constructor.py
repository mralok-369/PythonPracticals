class Employee:
    no_of_leave = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}."

    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leave = newLeaves

    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

harry = Employee("Harry Bhai",455,"instructor")
rohan = Employee("Rohan Das",4554,"Student")
karan = Employee.from_str("Karan-480-Student")
alok = Employee.from_str("Alok-1000-CSE")

print(karan.salary)
print(Employee.printdetails(alok))
print(Employee.printdetails(karan))
# print(harry.name)
# harry.change_leaves(34)
# print(harry.no_of_leave)
