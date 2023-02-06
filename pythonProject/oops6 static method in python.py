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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good " + string)

harry = Employee("Harry Bhai",455,"instructor")
rohan = Employee("Rohan Das",4554,"Student")
karan = Employee.from_str("Karan-480-Student")

karan.printgood("Alok")
Employee.printgood("Rohan")
