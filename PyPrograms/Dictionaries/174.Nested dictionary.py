laptop = {"Brand":"Macbook","OS":"Mac OS"}
mobile = {"Brand":"Iphone","OS":"IOS"}
Apple = {"laptop":laptop,
         "mobile":mobile
        }
print("Apple Products: ")
for x in Apple.items():
    print(x)