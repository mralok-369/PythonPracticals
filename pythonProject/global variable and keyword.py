l = 10 #global variable
def func1(n):
    # l = 5 #local variable
    global l
    l = l+20
    print(l)
    print(n,"i have printed")

func1("This is me")
print(l)