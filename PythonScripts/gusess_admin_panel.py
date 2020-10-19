#!/usr/bin/python
import urllib
from urllib import request
def asd():
    try:
        print()
        a = input("enter website to gusess : ")
        print()
        b = input("enter word list : ")
        b = b.replace("'",'')
        b = b.rstrip()
        print()
        c = open(b, 'r')
        d = c.readlines()
        for e in d:
            f = a + e
            try:
                urllib.request.urlopen(f)
                print(f)
            except:
                print("[-] Not Found")
        c.close()
    except Exception as ex:
        print(ex)
asd()
