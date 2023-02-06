list = ["iphone","mi","vivo","oneplus"]
print("Unsorted list: ",list)

def findLen(e):
    return len(e)

list.sort(key==findLen(list))
print("Insorted list: ",list)

list.sort(reverse=True,key=findLen(list))
print("Sorted list : ",list)