# *args and *kwargs

# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# function_name_print("Alok","Harry","Vishal","Alex","shivam")

def funargs(normale,*args,**kwargs):  # *args takes arguments as a tuple
    # print(type(args))
    print(normal)
    for item in args:
        print(item)

    print("\nhere are some legends")

    for key,value in kwargs.items():
        print(key,value)

har = ["Alok","Harry","Vishal","Alex","shivam","The Programmer"]
normal = 'these are all'
kw = {"rohan":"monitor","Alok":"programmer","number":145}
funargs(normal,*har,**kw)



