"""
iterable - __iter__() or __getitem__()
iterator - __next__()
iteration -
"""

# generator -> can be generated once
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h = "harry"
# print(h[0])
itr = iter(h) # generating iterator of h
print(itr.__next__())
print(itr.__next__())

# for c in h:
#     print(c)