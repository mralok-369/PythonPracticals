x = 40
def func():
    global x
    x = 50
print("value of x:",x)
func()
print("value of x after fun call",x)