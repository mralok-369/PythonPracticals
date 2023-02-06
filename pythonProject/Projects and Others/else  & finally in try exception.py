f1 = open("alok.txt")
try:
    f = open("does.txt")

except EOFError as e:
    print("Eof error occured",e)
# we can use multiple except block
except IOError as e:
    print("IO error occured",e)

else:
    print("this will run only if except is ot running")

finally:
    print("run this anyway")
    # f.close()
    f1.close()

print("Important stuff")