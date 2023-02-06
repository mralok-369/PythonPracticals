'''i=0
while(True):
    if(i+1<5):
        i=i+1
        continue
    print(i+1,"Hello World")
    if(i==19):
        break #stop the loop
    i=i+1
       '''
# quiz
'''taking input from user until entered number is less than 100 either its break the loop'''
while(True):
    inp = int(input("Enter a Number : "))
    if inp>100:
        print("congrats you have entred a number greater than 100")
        break
    else:
        print("try again")
        continue