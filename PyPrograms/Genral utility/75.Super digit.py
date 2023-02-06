n = int(input("Enter the number: "))
while(n>=10):
    x = n
    s = 0
    while(x>0):
        s = s+(x%10)
        x = x//10
    n = s
print("Super digit of the given number is ",n)