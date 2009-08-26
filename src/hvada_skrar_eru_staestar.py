# encoding: utf-8
import os, sys, operator

_listOfFiles=[]
_numberOfFiles = 3

def getlocaldata(sms,dr,flst):
    idx = 1
    
    for f in flst:
        fullf = os.path.join(dr,f)
        if os.path.islink(fullf): 
            continue
        if os.path.isfile(fullf):
            if len(_listOfFiles) == _numberOfFiles: # taka minnsta stakid
                for i in _listOfFiles:
                    print i[1]
                    print os.path.getsize(fullf)
                    print "--"
                    if i[1] < os.path.getsize(fullf):
                        _listOfFiles.remove(i)
                        tup = (fullf, os.path.getsize(fullf))
            else:
                tup = (fullf, os.path.getsize(fullf))
                _listOfFiles.append(tup)
                _listOfFiles.sort()
                
def dtstat(dtroot, number):
    _numberOfFiles = number
    sums = []
    os.path.walk(dtroot,getlocaldata,sums)

def main():
#    print "ello"
    
    report = dtstat('/home/gunnl/py/', 3)
    print _listOfFiles

if __name__== '__main__':
    main()