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

def timeFilter(s):
    pattern = re.compile(r'[:]')
    timi = pattern.split(s)
    return timi

def checkWeekday(t,w):
    for day in t:
        if w == day:
            return True        
    return False


def vinna(stimplanir, taxtar):
    dv = 0.0
    ev = 0.0
    yv = 0.0
    nv = 0.0
    for stimplun in stimplanir:
        arrDagsetning = dateFilter(stimplun[0])
        arrTimi = stimplun[1]
        timiInn = timeFilter(arrTimi[0])      
        timiUt = timeFilter(arrTimi[1])
        manNumer = manudurSemNumer(arrDagsetning[1])
        inn = datetime.datetime(int(arrDagsetning[2]), manNumer , int(arrDagsetning[0]), int(timiInn[0]), int(timiInn[1]))
        ut = datetime.datetime(int(arrDagsetning[2]), manNumer , int(arrDagsetning[0]), int(timiUt[0]), int(timiUt[1]))
        weekday = inn.weekday()
        for taxti in taxtar:
            taxtiTimi = taxti[1]
            print taxtiTimi           
            taxtiStart = datetime.datetime.time(datetime.datetime.strptime(taxtiTimi[0],"%H:%M"))
            taxtiEnds = datetime.datetime.time(datetime.datetime.strptime(taxtiTimi[1],"%H:%M"))
            print taxtiStart
            print taxtiEnds
            if checkWeekday(taxti[2],weekday):
                print True
               
        delta = ut - inn
        print "%3.2f"%(delta.seconds/3600.0)
    return [("dv", 1.0)]

vinna(stimplanir,taxtar)
