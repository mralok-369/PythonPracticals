import random
num = int(input("Enter the number of random no you want: "))
max = int(input("Enter the maximum value of random no: "))
print(num,"Random numbers b/w 0 to",max)
for i in range(num):
    print(random.randint(0,max))