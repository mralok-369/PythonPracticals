import time

initial = time.time()
# print(initial)

k = 0
while(k<45):
    print("Hello World")
    # time.sleep(2)   # its wait for given time like here 2 sec
    k+=1
print("while loop ran in",time.time()-initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("Hello World")
print("for loop ran in",time.time()-initial2,"seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)





