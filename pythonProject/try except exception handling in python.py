#try except and exception handling in python
print("Enter number 1")
num1 = input()
print("Enter number 2 ")
num2 = input()
try:
    print("sum of num1 and num2 is : ",
          int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")