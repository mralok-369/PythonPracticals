var1 = "Hello World" #string variable
var2 = 45  #int variable
var3 = 25.50 #float variable
print(var1)
print(var2)
print(var3)
print(type(var1))  #use of type function
print(type(var2))
print(type(var3))
var4 = "32" #its behave like a string variable
var5 = "48"

print(var2+var3)
print(var1+var4)
print(int(var4)+int(var5)) #typecasting of string variable to convert them into integer variable
                        #print(type(var1)) is the typecasting
"""
    str()
    int()
    float()
"""

print(10*"Hello World\n")
print(100* (int(var4)+int(var5)))

print("Enter Your number")
inpnum = input() #its taking input as a string variable
print("You Entered : ",inpnum)
print("After value  : ",int(inpnum)*10)

# Quiz Question
# make a calculator takes input as two number and add both number
print("Enter first number")
n1 = input()
print("Enter Second number")
n2 = input()
print("sum of both numbers is : ",int(n1)+int(n2))