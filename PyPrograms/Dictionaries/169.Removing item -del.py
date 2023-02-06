bike = {
    "Brand":"Bajaj",
    "Model":"Avenger",
    "Year":2019,
    "Engine":"220CC"
}
print("Bike details : ")
for x in bike.items():
    print(x)
del bike["Engine"]

print("Bike details after pop() : ")
for x in bike.items():
    print(x)

