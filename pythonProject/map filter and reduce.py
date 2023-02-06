#----------map function----------

# numbers = ["3","34","64"]
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(map(int,numbers))
# numbers = list(map(int,numbers))
# numbers[2]+=1
# print(numbers[2])
# def sq(a):
#     return a*a
# num = [2,3,5,6,76,5,3,6,2]
# square = list(map(sq,num))
# print(square)
# num = [2,3,5,6,7,5,3,6,2]
# square = list(map(lambda x: x*x,num))
# print(square)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# func = [square,cube]
# # num = [2,3,5,6,7,5,3,6,2]
# for i in range(5):
#     val = list(map(lambda x: x(i),func))
#     print(val)


# ------------filter function------------
list1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_tahn_5 = list(filter(is_greater_5,list1))
print(gr_tahn_5)

# ------Reduce Function-------
from functools import reduce

list2 = [1,2,3,4]
num = reduce(lambda x,y:x+y,list2)
print(num)

# num = 0
# for i in list2:
#     num = num+i
# print(num)








