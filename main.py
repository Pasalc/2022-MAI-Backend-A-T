from cache import * 
if __name__=='__main__':
    test=LRU()
    print(test.get("We"))
    test.set("We","Wi")
    print(test.get("We"))
    test.rem("We")
    print(test.get("We"))

