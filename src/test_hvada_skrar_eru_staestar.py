# encoding: utf-8
import unittest, hvada_skrar_eru_staestar

class HvadaSkrarEruStaestarTestCase(unittest.TestCase):    
    path = "/home/gunnl/py/"
    numberOfFiles = 3
       
    def testListFiles(self):
        utkoma = hvada_skrar_eru_staestar.listFiles(self.path, self.numberOfFiles)
        self.failUnless(utkoma == True, 'Test féll')
        
    def testTest(self):
        utkoma = hvada_skrar_eru_staestar.test(self.path)
        self.failUnless(utkoma == True, 'Test féll')

if __name__ == '__main__': unittest.main()
