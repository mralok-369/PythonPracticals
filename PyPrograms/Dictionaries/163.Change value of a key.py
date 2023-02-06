bike = {
    "Brand":"Bajaj",
    "Model":"Avenger",
    "Year":2019,
    "Engine":"220CC"
}
print("Dictionary data: ")
for x in bike.items():
    print(x)
bike["Model"] = "Pulser"

print("Bike details after modified : ")
for x in bike.items():
    print(x)
