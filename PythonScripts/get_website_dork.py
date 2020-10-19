#!/usr/bin/python
try:
    import googlesearch
    from googlesearch import *
except Exception as ex:
    print(str(ex))

def asd():
    try:
        print()
        a = input("enter website dork : ")
        print()
        b = int(input("enter end of number : "))
        print()
        for c in search(a, stop=b):
            print(c)
    except Exception as exc:
        print(str(exc))
asd()
