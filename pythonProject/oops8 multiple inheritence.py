class Employee:
    var = 8
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

class Player:
    var = 9
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}."

class CoolProgrammer(Employee,Player):
    languages = "C++"
    def printLanguage(self):
        return self.languages

harry = Employee("Harry Bhai",255,"instructor")
rohan = Employee("Rohan Das",455,"Student")

shubham = Player("Shubham",["Cricket"])
karan = CoolProgrammer("Karan",8999,"CoolProgrammer")
# det = karan.printdetails()
# print(karan.printLanguage())
# print(det)
print(karan.var)