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

def regexp(s):
    pattern = re.compile(r'[. ]')
    manudur = pattern.split(s)
    return manudur[1]

def vinna(stimplanir, taxtar):  
    for stimplun in stimplanir:
        print regexp(stimplun[0])
        print manudurSemNumer(regexp(stimplun[0]))
    return [("dv",1.0)]