n = int(input("Enter no of elements: "))
list = []
for item in range(n):
    list.append(int(input("Enter number: ")))
print("list : ",list)
n1 = list.count(int(input("Enter number to find occurance: ")))
print("total occurance : ",n1)

