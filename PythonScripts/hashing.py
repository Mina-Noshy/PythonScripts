#!/usr/bin/python
import hashlib
def asd():
    try:
        print()
        a = input("enter word to hash : ")
        print()
        x = hashlib.algorithms_available
        print("press any key to view hash types : ")
        input()
        for y in x:
            print(y)
        print()
        b = input("enter hash type : ")
        print()
        c = hashlib.new(b)
        c.update(a.encode("utf-8"))
        d = c.hexdigest()
        print()
        print(d)
        print()
        z = input("try again (y \ n) : ")
        if z == "Y" or z == "y":
            asd()
        else:
            print()
            print("good bye ..")
            print()
    except Exception as ex:
        print("[ERR] " + str(ex) + " !")
        print()
asd()
