def func(*proLang):
    print("Programming language known: ")
    for x in proLang:
        print(x)

print("1st function call :")
func("c","c++")
print("2nd function call :")
func("c","java","python")
print("3rd function call :")
func("c","c++","java","python")