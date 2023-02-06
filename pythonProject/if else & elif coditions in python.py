"""
var1 = 6
var2 = 56
print("Enter any number")
var3 = int(input())
if var3>var2:
    print("greater")
elif var3==var2:
    print("Equal")
else:
    print("lesser")
"""
"""
list1 = [5,7,3]
print(15 not in list1)
if 15 not in list1:
    print("No its not in the list") """

#quiz = enter your age if>18 can drive if<18 cannot drive if=18 we cannot decide you come first then we decide
print("Enter your age")
age = int(input())
if age>18:
    print("Yes you can drive")
elif age==18:
    print("We cannot decide before seeing you")
else:
    print("No you cannot drive")