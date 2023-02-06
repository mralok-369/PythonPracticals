# Object introspection is knowing details about any objects like as from which class what types how it's stored'
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def printemail(self):
        pass

    @property  #property decoraters
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # setters
    def email(self,string):
        print("Setting now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter #deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
# print(skillf.email)
# print(type(skillf))
# print(type("This is a string"))
# print(id("This is a string"))
# print(id("that that"))

o = "This is a string"
# print(dir(o))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))
print(len(inspect.getmembers(skillf)))

# qiiz
# Learn inspect module from google and
# using inspect module built a function that inspect a object
# like print all the attribue of the object
# like print all the class variables of the object
# like print all the instance variables of the object