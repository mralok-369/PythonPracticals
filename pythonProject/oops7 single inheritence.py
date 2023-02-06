# Abstaraction - breaking the program in many pieces
# Encapsulation - Hiding all functinality from the user
class Employee:
    no_of_leave = 8  #class variable

    #Constructor of employee
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    #printdetails fun for showing det of constructor
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}."
    #class method for change leave
    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leave = newLeaves
    #class method to work as a alternative constructor
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    #static method
    @staticmethod
    def printgood(string):
        print("this is good " + string)

class Programmer(Employee):
    no_of_holidays_packages = 56
    #constructor
    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.lannguages = languages
    #method to print det of prog
    def printprog(self):
        return f"The Programmer is {self.name}. Salary is {self.salary}. and role is {self.role}.The languages are {self.lannguages}"

harry = Employee("Harry Bhai",455,"instructor")
rohan = Employee("Rohan Das",4554,"Student")

shubham = Programmer("Shubham",555,"Programmer",['python'])
karan = Programmer("karan",777,"Programmer",['python',"Cpp","Java"])
print(karan.printprog())
print(Programmer.no_of_holidays_packages)
# print(karan.printdetails())
