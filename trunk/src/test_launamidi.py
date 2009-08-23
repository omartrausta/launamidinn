# encoding: utf-8
import unittest, launamidi

class ProductTestCase(unittest.TestCase):    
    _stimplanir = [("17.�g�st 2009",("09:00","10:00"))]
    _taxtar = [("dv",("09:00","17:00"),[0,1,2,3,4])]
    _nidurstada = [("dv",1.0)]
    def testVinna(self):
        utkoma = launamidi.vinna(self._stimplanir, self._taxtar)
        self.failUnless(utkoma == self._nidurstada, 'Utreikningar fellu')

if __name__ == '__main__': unittest.main()