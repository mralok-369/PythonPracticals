def linear(list, n, val):
    for i in range(0, n):
        if (list[i] == val):
            return i
    return -1

list = [1, 3, 5, 4, 7, 9]
val = 7
n = len(list)
ans = linear(list, n, val)
if (ans == -1):
    print("Element not found")
else:
    print("Element found at index: ", ans)
