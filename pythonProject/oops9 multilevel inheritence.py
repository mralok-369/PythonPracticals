class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    guitar = 5
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    basketball = 10
    def isdance(self):
        return f"Jackson yeah !! " \
               f"Yes i dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball) # first it search in his own class then above
print(harry.guitar)

# quiz multiple inheritence
# electronic device
# pocket gadgets
# phones