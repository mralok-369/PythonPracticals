class Employee:
    no_of_leave = 8 #same for all object of this class
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "instructure"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "student"

print(rohan.no_of_leave)
# Employee.no_of_leave = 9
# print(Employee.no_of_leave)
print(rohan.__dict__)
rohan.no_of_leave = 9
print(rohan.__dict__)
print(rohan.no_of_leave)