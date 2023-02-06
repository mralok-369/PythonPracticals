bike = {
    "Brand":"Bajaj",
    "Model":"Avenger",
    "Year":2019,
    "Engine":"220CC"
}
print("Dictionary data: ")
for x in bike.items():
    print(x)
bike.update({"Color":"Jet Black"})

print("Length of bike dictionary: ",len(bike))
