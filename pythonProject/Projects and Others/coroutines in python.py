def searcher():
    import time
    # some 4 second time consuming task
    book = "this is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in book")
        else:
            print("text is not in the book")

search = searcher()
print("search started")
next(search)
print("next method run")
search.send("harry")

search.close()
# search.send("alok")  # after closing seearch we cannot run send method it will throw error

# input("press any key : ")
# search.send("harry and")
# input("press any key : ")
# search.send("thi si")
# input("press any key : ")
# search.send("joker")
# input("press any key : ")
# search.send("i love you")