def outerfact():
    print("Hello from outer function")

    def innerfact():
        print("Hello from inner function")
    innerfact()
outerfact()