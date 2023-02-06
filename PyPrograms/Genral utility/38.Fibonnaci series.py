def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))

nterms = int(input("ENter number of terms: "))
if nterms<=0:
    print("Please enter a positive number")
else:
    print("Fibonacci series: ")
    for i in range(nterms):
        print(recur_fibo(i))