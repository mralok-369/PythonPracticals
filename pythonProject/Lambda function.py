# Anonymous or lambda function
# lambda is a one linear function that's why it is called anonymous function
# minus = lambda x, y: x-y
# print(minus(9,4))

# def a_first(a):
#     return a[1]

a = [[1,4],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)