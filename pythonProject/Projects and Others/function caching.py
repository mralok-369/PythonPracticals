import time
from functools import lru_cache

# function caching is a technique to save run value of a func so if the function called again the executes fast

@lru_cache(maxsize=3)
def some_work(n):
    # some task taking n second
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("done......calling again")
    input("press any key")
    some_work(3)
    print("calling again")