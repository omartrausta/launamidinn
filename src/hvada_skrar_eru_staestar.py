# encoding: utf-8
import os.path

def listFiles(path,numberOfFiles):
    files = os.listdir(path)
    
    #listOfFiles = []
    
    for file in files:
        f = path + file
        if os.path.exists(f):
            #
            #if os.path.isfile(f):
            print f + " " 
            print os.path.getsize(f)
            #listOfFiles.append(f)
        else:
            print "no file!"
           

    return True

def callback( arg, dirname, fnames ):
    sum = 0
    for file in fnames:
        sum += os.path.getsize(file)
    arg.append(sum)


def test(path):
    arglist = []
    os.path.walk("./",callback,arglist)

    sum = 0
    for value in arglist:
        sum += value

    print "Size of directory:",sum
    return True
