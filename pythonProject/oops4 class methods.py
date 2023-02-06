class Employee:
    no_of_leave = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}"

    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leave = newLeaves


harry = Employee("Harry Bhai",455,"instructor")
rohan = Employee("Rohan Das",4554,"Student")

# print(harry.name)
harry.change_leaves(34)
print(harry.no_of_leave)
