import os

# print(dir(os))  // returns methods of os module
# print(os.getcwd()) // returns current working directory
# os.chdir("c://")  // change directory
# print(os.getcwd())
# f = open("alok.txt")
# print(os.listdir())  // returns list of folder in current directory
# print(os.listdir("c://"))  // returns list of folder and file in given path directory
# os.mkdir("ALEX")  # make directory
# os.mkdirs("ALEX/ALOK")  # make directory in directory
# os.rename("harry.txt","alex.txt")  # rename file or folder
# print(os.environ.get('path')) # return environment variable path
# print(os.path.join("c:/","/alex.txt")) # to oin two path
# print(os.path.exists("C://Program Files"))  # check that the given directory exist or not
print(os.path.isdir("C://Program Files"))  # to check it is directory or file
print(os.path.isfile("C://Program Files"))  # to check it is directory or file
