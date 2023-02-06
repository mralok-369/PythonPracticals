# Health management system
# 3 clients - harrry rohan and hammad
'''def getdate():
    import datetime
    return datetime.datetime.now()

total 6 files
write a function that when executed takes as input client name
[time]Table caseover
onr more function to reterive excercise or food for any client'''

# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c = int(input("Enter 1 for Excercise and 2 for Food"))
#         if c==1:
#             value = input("Type")


def getdatetime():
    import datetime
    return datetime.datetime.now()

def callHealthManagementSystem():
    print("Welcome to HMS\n");
    operation = ( "Retrive","Write" )
    user = ("Mukesh","Gautam","Praveen")
    log = ("Food_taken","Exercise_done")
    while True:
        n1 = input("What function you want to do\nPress 1 for Retrive, 2 For Write:\n")
        if int(n1) == 1 or int(n1) == 2:
            while True:
                n2 = input("Press 1 for Mukesh, 2 for Gautam, and 3 for Praveen\n")
                if int(n2) == 1 or int(n2) == 2 or int(n2) == 3:
                    while True:
                        n3 = input("Press 1 for Food, 2 for Exercise\n")
                        if int(n3) == 1 or int(n3) == 2:
                            filename = user[int(n2)-1]+"_"+log[int(n3)-1]+".txt"
                            if int(n1) == 2:
                                n4 = input("What " + log[int(n3) - 1] + " by " + user[int(n2) - 1]+":\n")
                                with open(filename,"a+") as f:
                                    f.write("["+str(getdatetime())+"] "+ n4+"\n")
                                    print("details logged successfully")
                            else:
                                try:
                                    with open(filename,"rt") as f:
                                        filecontent = f.read()
                                        print (filecontent)
                                except Exception as e:
                                    print(e)
                            break
                        else:
                            print("Wrong choice try again")
                    break
                else:
                    print("Wrong user choose try again")
            break
        else:
            print("Wrong Operation call")

callHealthManagementSystem()