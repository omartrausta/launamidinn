# encoding: utf-8
import unittest, launamidi

class ProductTestCase(unittest.TestCase):    
    stimplanir = [("17.ágúst 2009",("09:00","10:00"))]
    taxtar = [("dv",("09:00","17:00"),[0,1,2,3,4])]
    nidurstada = [("dv",1.0)]
    def testVinna(self):
        utkoma = launamidi.vinna(self.stimplanir, self.taxtar)
        self.failUnless(utkoma == self.nidurstada, 'Utreikningar fellu')

if __name__ == '__main__': unittest.main()