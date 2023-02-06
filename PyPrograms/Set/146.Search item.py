myset = {"Apple","Banana","Cherry","Dragon","Fruit"}
search = input("Enter the item you want to search: ")
if search in myset:
    print("Yes,",search,"is in the set.")
else:
    print("No,",search,"isn't in the set.")