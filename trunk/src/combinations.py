#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def moguleikar(l, x):
    if not l or not x or len(l) < x:
        yield (())
    elif len(l) == x:
        yield tuple(l)
    elif len(l) > x:
        Z = (l[0],)
        for c in moguleikar(l[1:], x-1):
            yield Z + c
        for c in moguleikar(l[1:], x):
            yield c

def work(l, x):
    listi = []
    for m in moguleikar(l, x):
        listi.append(m)
    return listi
    
def main():
    litir=["gulur","rauður","grænn","blár","svartur","hvítur","fjólublár"] 
    result = work(litir, 2)
    for r in result:
        print r[0].encode("utf-8"), r[1].encode("utf-8")

if __name__== "__main__": main()
