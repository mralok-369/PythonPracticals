# for loop in python
list1 = [["Harry",1],["Larry",2],["Carry",6],["Marry",250],["Narry",10]]
dict1 = dict(list1)  #typecasting list1 into dict1(dictionary)
print(dict1)
'''for item,lolypop in list1:     #for list iteration
    print(item,"eats",lolypop,"lollypop") '''
'''for item, lollypop in dict1.items(): #for dictionary iteration
    print(item, "eats" ,lollypop, "lollypops")'''


# quiz 2
'''create a list of items and print only them which are greater than 6'''
items = [int,float,"alok",5,3,3,22,21,64,23,233,23]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)