# encoding: utf-8
import os, sys, operator

_listOfFiles=[]

def getlocaldata(sms,dr,flst):
    for f in flst:
        fullf = os.path.join(dr,f)
        if os.path.isfile(fullf): 
            tup = (fullf, os.path.getsize(fullf))
            _listOfFiles.append(tup)
    tmp = sorted(_listOfFiles, key=operator.itemgetter(1))
    sms[1] = tmp[operator.neg(sms[0]):] 
                
def dtstat(dtroot, number):
    _numberOfFiles = number
    sums = [number,0]
    os.path.walk(dtroot,getlocaldata,sums)
    return sums[1]
    
def main():
    root, numbers = sys.argv[1:]
    report = dtstat(root, int(numbers))
    print report

if __name__== "__main__": main()