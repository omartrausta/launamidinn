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

def main(): 
    litir=["gulur","rauður","grænn","blár","svartur","hvítur","fjólublár"]    
    for m in moguleikar(litir, 2):
        print "('", m[0], "','",m[1],"')"
    
if __name__== "__main__": main()
