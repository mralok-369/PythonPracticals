def interpolation(list, low, high, val):
    if (low <= high and val >= list[low] and val <= list[high]):
        pos = low + ((high - low) // (list[high] - list[low]) *(val - list[low]))
        if list[pos] == val:
            return pos
        if list[pos] < val:
            return interpolation(list, pos + 1, high, val)
        if list[pos] > val:
            return interpolation(list, low,pos - 1, val)
    return -1
# Driver code
list = [10, 12, 13, 16, 18, 19, 20]
n = len(list)
# Element to be searched
val = 13
ans = interpolation(list, 0, n - 1, val)
if ans != -1:
    print("Element found at indeval", ans)
else:
    print("Element not found")

