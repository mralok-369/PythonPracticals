'''
    # Types of operators in python
    Arithmetic operator = +,-,*,/,//,**
    Comparison operator
    Logical operator
    identity operator
    Membership operator
    Bitwise operator
'''
print("Arithmetic operators")
print("5 + 6 is",5+6)
print("5 - 6 is",5-6)
print("5 * 6 is",5*6)
print("5 / 6 is",5/6)
print("7 % 3 is",7%3)
print("5 ** 3 is",5**3)
print("15 // 6 is",15//6)

print("Assignment operators")
x = 5
print(x)
x+=7 # x = x+7
x%=5 #x-=2, x*=4,etc
print(x)

print("Comparision operators")
i=8
print(i==5)
print(i!=5)
print(i>5)
print(i>=5)
print(i<5)
print(i<=5)

print("Logical operators")
a = True
b = False
print(a and a)
print(a and b)
print(a or a)
print(a or b)
print(a is b)
print(a is not b)

print("Membership operators")
list = [3, 3,2, 2,39, 33, 35,32]
print(32 in list)
print(324 in list)
print(324 not in list)

print("Bitwise operators")
print(0 & 1)
print(0 | 1)
print(0 | 3)