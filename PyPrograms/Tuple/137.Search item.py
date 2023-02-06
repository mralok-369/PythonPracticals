t1 = ("Iphone","MI","VIVO","OnePlus","Oppo","C","C++","C#","Python")
search = input("Enter item to be searched: ")
if search in t1:
    print("Yes, ",search,"is in the tuple.")
else:
    print("No, ",search,"isn't in the tuple.")