#!/usr/bin/python
import hashlib
def asd():
    try:
        print()
        a = str(input("enter hash to gusess : "))
        print()
        b = input("enter word list : ")
        b = b.replace("'",'')
        b = b.rstrip()
        c = open(b, 'r')
        c = c.readlines()
        print()
        d = hashlib.algorithms_available
        d = list(d)
        for e in d:
            print("=======================================")
            for f in c:
                f = f.replace('\n','')
                g = hashlib.new(e)
                g.update(f.encode("utf-8"))
                h = g.hexdigest()
                if h == a:
                    print("[+] Found ===> " + e + " => " + f)
                else:
                    print("[-] Not Found")
        c.close()
    except Exception as ex:
        print(str(ex))
asd()
