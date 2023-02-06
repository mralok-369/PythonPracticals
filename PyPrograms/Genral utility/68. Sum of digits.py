n = int(input("Enter number: "))
sum = 0
while(n>0):
    dig = n%10
    sum+=dig
    n = n//10
print("Sum of digits of number is = ",sum)