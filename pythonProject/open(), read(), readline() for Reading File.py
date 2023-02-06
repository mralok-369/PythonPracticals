f = open("alok.txt","rt") #OPEN FUCTION always return a pointer
print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())


# content = f.read(344) #344 is the no character which read from the file

# for line in f:
#     print(line,end="")

# print(content)
# content = f.read(344) #it reads from that point from where first read function end
# print("2",content)
f.close()