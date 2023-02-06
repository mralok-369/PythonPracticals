# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# list comprehensions
# ls = [i for i in range(100)]
# ls = [i for i in range(100) if i%3==0]
# print(ls)

# dictionary comprehensions
# dict1 = {i:f"item{i}" for i in range(100)}
# dict1 = {i:f"item {i}" for i in range(100) if i%3==0}
dict1 = {i:f"Item {i}" for i in range(5)}
dict2 = {value:key for key,value in dict1.items()} # reverse of dict1
print(dict1,"\n",dict2)

# set comprehensions
dresses = {dress for dress in ["dress1","dress2","dress1",
                               "dress2","dress1","dress2"]}
print(dresses)

# generator comprehensions
evens = (i for i in range(100) if i%2==0)
print(type(evens))
# print(evens.__next__())
for item in evens:
    print(item)