# f = open("alok.txt","a")
# a = f.write("alok is a bad boy\n")
# print(a)
# f.close()

#handle both read and write mood
f = open("alok.txt","r+")
print(f.read())
f.write("thank you ")
print(f.read())