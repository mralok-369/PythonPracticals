str1 = input("ENter string : ")
str1 = str1.casefold()
revstr = reversed(str1)
if list(str1) == list(revstr):
    print("The string is Palindrome")
else:
    print("The string is not palindreome")