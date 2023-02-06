# Public - Access for anybody
# Protected - Access for some limited user
# Private - Cannot access by anyone
class Employee:
    no_of_leave = 8 # Public variable
    var = 8     # Public variable
    _protect = 9  # Protected variable
    __Private = 98  # Private variable

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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)

emp = Employee("harry",343,"Programmer")
print(emp._protect)
# print(emp._Employee__private)