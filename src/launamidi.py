# encoding: utf-8
import datetime
import time
import operator
import re


stimplanir = [("17.ágúst 2009", ("09:00", "10:35"))]
taxtar = [("dv", ("09:00", "17:00"), [0, 1, 2, 3, 4])]

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


def checkWeekday(t,w):
    for day in t:
        if w == day:
            return True        
    return False


def vinna(stimplanir, taxtar):
    for stimplun in stimplanir:
        stimplDagsetning = dateFilter(stimplun[0])
        stimplTimi = stimplun[1]
        manNumer = manudurSemNumer(stimplDagsetning[1])
        innDags = datetime.date(int(stimplDagsetning[2]), manNumer , int(stimplDagsetning[0]))
        utDags = datetime.date(int(stimplDagsetning[2]), manNumer , int(stimplDagsetning[0]))
        stimpunInn = datetime.datetime.strptime(stimplTimi[0],"%H:%M")
        stimpunUt = datetime.datetime.strptime(stimplTimi[1],"%H:%M")
        print stimpunInn
        print stimpunUt
        weekday = innDags.weekday()
        for taxti in taxtar:
            taxtiTimi = taxti[1]
            print taxtiTimi           
            taxtiStart = datetime.datetime.strptime(taxtiTimi[0],"%H:%M")
            taxtiEnds = datetime.datetime.strptime(taxtiTimi[1],"%H:%M")
            print taxtiStart
            print taxtiEnds
            if checkWeekday(taxti[2],weekday):
                
               
        delta = stimpunUt - stimpunInn
        print "%3.2f"%(delta.seconds/3600.0)
    return [("dv", 1.0)]

vinna(stimplanir,taxtar)
