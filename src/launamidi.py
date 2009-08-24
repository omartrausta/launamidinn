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

def dateFilter(s):
    pattern = re.compile(r'[. ]')
    manudur = pattern.split(s)
    return manudur

def timeFilter(s):
    pattern = re.compile(r'[:]')
    timi = pattern.split(s)
    return timi

def vinna(stimplanir, taxtar):  
    for stimplun in stimplanir:
        arrDagsetning = dateFilter(stimplun[0])
        arrTimi = stimplun[1]
        timiInn = timeFilter(arrTimi[0])
        timiUt = timeFilter(arrTimi[1])
        manNumer = manudurSemNumer(arrDagsetning[1])
        inn = datetime.datetime(int(arrDagsetning[2]), manNumer ,int(arrDagsetning[0]), int(timiInn[0]), int(timiInn[1]))
        ut = datetime.datetime(int(arrDagsetning[2]), manNumer ,int(arrDagsetning[0]), int(timiUt[0]), int(timiUt[1]))
        print inn
        print ut
        print ut - inn
    return [("dv",1.0)]