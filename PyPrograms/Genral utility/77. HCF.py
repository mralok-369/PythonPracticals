def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(a,a%b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
ans = gcd(a,b)
print("GCD = ",ans)