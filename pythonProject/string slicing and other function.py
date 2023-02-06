mystr = "alok is a good boy"
print(len(mystr)) #using len fuction to find string length
"""print(mystr[0:4])
print(mystr[0:4:2])
print(mystr[0:])
print(mystr[0::2])
print(mystr[::1])
print(mystr[0:18])
"""
"""
print(mystr[-4:])
print(mystr[-4:-2])
print(mystr[::-1])
print(mystr[::-2])
"""
print(mystr.isalnum()) # isalnum stand for alphanumeric function
print(mystr.isalpha()) # isalnum stand for alpha function
print(mystr.endswith("boy")) #endswith stand for checking string is ended with given string or not
print(mystr.count("o")) # counting number of character or word in the string
print(mystr.capitalize()) #capitalize the first letter of string
print(mystr.find("is"))  #find the given word or ch in string and return the first block of word or ch
print(mystr.lower()) # convert string in lowercase letter
print(mystr.upper())  #convert string in uppercase letter
print(mystr.replace("alok","harry")) # replace the given word in the string

