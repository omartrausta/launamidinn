# encoding: utf-8
import os.path

#def listFiles(path,numberOfFiles):
#    files = os.listdir(path)
    
    #listOfFiles = []
    
#    for file in files:
 #       f = path + file
  #      if os.path.exists(f):
            #
            #if os.path.isfile(f):
   #         print f + " " 
    #        print os.path.getsize(f)
            #listOfFiles.append(f)
     #   else:
      #      print "no file!"
           

#    #return True

#def callback( arg, dirname, fnames ):
#    sum = 0
#    for file in fnames:
#        sum += os.path.getsize(file)
#    arg.append(sum)


#def test(path):
#    arglist = []
#    os.path.walk("./",callback,arglist)

#    sum = 0
#    for value in arglist:
#        sum += value

#    print "Size of directory:",sum
#    return True


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