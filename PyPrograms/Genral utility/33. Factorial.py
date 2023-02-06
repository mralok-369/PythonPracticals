def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)
num = int(input("ENter number to find factorial: "))
if num < 0:
    print("Cannot find it's factorial")
elif num==0:
    print("fcatorial of 0 is 1")
else :
    print("Factorial of ",num ,"is : ",factorial(num))

