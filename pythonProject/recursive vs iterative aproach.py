# def fact(n):
#     if n<=1:
#         return 1
#     else:
#         return n* fact(n-1)
# n = int(input("Enter a number: "))
# print("factorial of",n,"is = ",fact(n))

#fibonacci series
def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input("Enter a number: "))
print("fibonacci series: \n",fibonacci(n))
