numbers = [1,3,6,2,7,5,8,4,9,0]
result = filter(lambda x:x<5,numbers)
print("Number list",numbers)
print("Numbers smaller than 5 in the list are: ")
print(list(result))