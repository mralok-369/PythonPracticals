bike = {
    "Brand":"Bajaj",
    "Model":"Avenger",
    "Year":2019,
    "Engine":"220CC"
}
search = input("Enter key to be searched: ")
if search in bike:
    print("Yes",search,"is in the bike dict")
else:
    print("No",search,"isn't in the bike dictionary.")
