# pattern printing
# input = integer n
# Boolean = True or False
# if true then print
# *
# * *
# * * *
# if false then
# ***
# **
# *
n = int(input("Enter number of rows: "))
print("Enter either 0 or 1: ")
choice = int(input())
ch = bool(choice)
if ch == True:
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif ch == False:
    for i in range(1,n+1):
        for j in range(n+1,i,-1):
            print("*",end=" ")
        print()

