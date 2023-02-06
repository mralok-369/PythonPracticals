# f string
import math

me = "Alok"
a1 = 3
# a = "this is %s %s"%(me,a1)
# a = "this is {1} {0}"
# b = a.format(me,a1)
# print(b)

a = f"this is {me} {a1} {math.cos(45)}"
print(a)

# explore time module and use time function which tell us about program running time
# pip install time