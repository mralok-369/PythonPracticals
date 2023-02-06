a = 9
b = 8
c = sum((a,b)) # built in function
print(c)

# user defined function
def func1():
    print("Hello you are in func1")

func1()

def function2(a,b):
    """this is the function which will calculate average of two numbers""" # this line is docstring
    avg = (a+b)/2
    return avg
v = function2(5,7)
print(v)
print(function2.__doc__)