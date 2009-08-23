# encoding: utf-8
import datetime
import operator
import re

_manudir = {'janúar':1,
                'febrúar':2,
                'mars':3,
                'apríl':4,
                'maí':5,
                'júní':6,
                'júlí':7,
                'ágúst':8,
                'september':9,
                'október':10,
                'nóvember':11,
                'desember':12}

def manudurSemNumer(manudur):
    return _manudir.get(manudur)

#
def regexp(s):
    #split
    #s = '<html><head><title>Title</title>'
    pattern = re.compile('.')
    print pattern.split(s)

def vinna(stimplanir, taxtar):
    
#    print manudurSemNumer('febrúar')
    
    for stimplun in stimplanir:
        for tup in stimplun:
            print 
            print type(tup)
            #print regexp(tup[1])


    
    return [("dv",1.0)]