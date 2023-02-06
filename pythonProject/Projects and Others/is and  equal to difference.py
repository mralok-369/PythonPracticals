# == -> value equality -> two objects have the same value
# is -> reference equality -> two references refer to the same objects

a = [6, 4, "34"]
b = [6, 4, "34"]
print(a is b)
print(b is a)
print(a == b)
print(b == a)
