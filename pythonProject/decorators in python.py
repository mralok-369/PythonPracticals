# def function1():
#     print("subscribe now")
#
# func2 = function1
# del function1
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
# a = funcret(1)
# print(a)

# def executor(func):
#     func("this")
#
# executor(print)

def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def who_is_alok():
    print("Alok is a good boy")

# who_is_alok = dec1(who_is_alok)
who_is_alok()