# raise keyword
# a = input("what is your name : ")
# b = input("how much do you earn : ")
# if int(b) == 0:
#     raise ZeroDivisionError("b is zero so stopping the program")
# if a.isnumeric():
#     raise Exception("Number are not allowed")
# print(f"Hello {a}")
# 1000 lines taking 1 hour

# Task -> write about 2 built in exception
c = input("Enter your name : \n")
try:
    print(a)
except Exception as e:
    if c == "harry":
        raise ValueError("Harry is blocked he is not allowed")
    print("Exception handled")