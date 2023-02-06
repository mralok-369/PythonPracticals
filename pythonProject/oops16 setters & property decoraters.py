class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def printemail(self):
        pass

    @property  #property decoraters can help a metod to run as a attribute not as a function
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter # setters set the value of any method after taking argument
    def email(self,string):
        print("Setting now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter #deleter to set the value of f&lname to none
    def email(self):
        self.fname = None
        self.lname = None



# at run time we pass fname and lname then the constructor ran
hindustani_supporter = Employee("Hindustani","Supporter")
# nikhil_raj_pandey = Employee("Nikhil","Raj")

# print(hindustani_supporter.explain())
print(hindustani_supporter.email) # print using property decorator
# hindustani_supporter.fname = "US" #HERE the value of fname remains unchanged
hindustani_supporter.fname = "US" #after creating a email method when we set the value of f&lname will changed
print(hindustani_supporter.email)

hindustani_supporter.email = "this.that@codewithharry.com" #set the value of email attribute using setters
# print(hindustani_supporter.fname)
# print(hindustani_supporter.lname)
print(hindustani_supporter.email)

#if i want to delete the value of email attribute then i have to make a deletor
del hindustani_supporter.email #delete the value of email attribute using deleter
print(hindustani_supporter.email)

hindustani_supporter.email = "harry.perry@codewithharry.com"
print(hindustani_supporter.email)