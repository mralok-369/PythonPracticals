#Excercise 2 = faulti calculator
"""
    Design a calculator which will correctly solve all the problems except the following one:
     45*3=555, 56+9 =77, 56/4=6
     your program should take operator and two numbers as input from the user and then return the result
"""
print("Enter first number :")
a = int(input())
print("Enter second number : ")
b = int(input())
print("Enter your operator ('+' or '-' or '*' or '/')")
opt = input()
if opt == '+':
    if a==56 and b==9:
        print("77")
    else:
        print(a+b)
elif opt == '-':
    if a>b:
        print(a-b)
    else:
        print(b-a)
elif opt == '*':
    if a==45 and b==3:
        print("555")
    else:
        print(a*b)
elif opt == '/':
    if a==56 and b==4:
        print("6")
    else:
        print(a/b)
else:
    print("Enter valid operator")


