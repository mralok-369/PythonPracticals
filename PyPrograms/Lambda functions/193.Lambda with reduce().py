from functools import reduce
numbers = [1,2,3,4,5]
prod=reduce(lambda x,y: x*y,numbers)
print("Product of all numbers in the list: ",prod)