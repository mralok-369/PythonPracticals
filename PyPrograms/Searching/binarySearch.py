def binary(list, val, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid] == val:
            return mid
        elif list[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1
list = [1, 3, 5, 7, 9]
val = 5
ans = binary(list, val, 0, len(list) - 1)
if ans != -1:
    print("Element is present at index " + ans)
else:
    print("Not found")
