fruits = ["Apple","Banana","Cherry","Dragon","Fruit"]
search = input("Enter item to searched: ")
if search in fruits:
    print("Yes",search,"is in the list.")
else:
    print("No", search, "isn't in the list.")