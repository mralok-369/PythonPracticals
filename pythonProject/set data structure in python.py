s = set()
#print(type(s))
#s_from_list = set({1,2,3,4})
#l= {1,2,3,4}
#s_from_list = set(l)
#print(s_from_list)
#print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2) #removing any element from set
#s1= s.union({1,2,3})  #find union of the sets
#s1 = s.intersection({1,2,3}) #finding intersection of sets
#print(s,s1)
"""print(len(s)) # length of any set
print(min(s)) # min value of any set
print(max(s)) # max value of any set"""

s1 = {4,6}
print(s.isdisjoint(s1))


