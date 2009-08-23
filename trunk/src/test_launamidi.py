# encoding: utf-8
import unittest, launamidi

class ProductTestCase(unittest.TestCase):
    stimlanir = [("17.�g�st 2009",("09:00","10:00"))]
    taxtar = [("dv",("09:00","17:00"),[0,1,2,3,4])]
    nidurstada = [("dv",1.0)]
    
    def testVinna(self):
        utkoma = launamidi.vinna(stimplanir, taxtar)
        self.failUnless(utkoma == nidurstada, 'Utreikningar fellu')

if __name__ == '__main__': unittest.main()