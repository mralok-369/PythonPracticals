bike = {
    "Brand":"Bajaj",
    "Model":"Avenger",
    "Year":2019,
    "Engine":"220CC"
}
print("Bike details : ")
for x in bike.items():
    print(x)
bike.clear()

print("Bike details after clear() : ")
# for x in bike.items():
#     print(x)
print(bike)
