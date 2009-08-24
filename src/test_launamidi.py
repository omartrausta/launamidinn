# encoding: utf-8
import unittest, launamidi

class LaunamidarTestCase(unittest.TestCase):    
    stimplanir = [("17.ágúst 2009", ("09:00", "10:00"))]
    taxtar = [("dv", ("09:00", "17:00"), [0, 1, 2, 3, 4])]
    nidurstada = [("dv", 1.0)]
    arrDagsetning = ['17', 'ágúst', '2009']
       
    def testVinna(self):
        utkoma = launamidi.vinna(self.stimplanir, self.taxtar)
        self.failUnless(utkoma == self.nidurstada, 'Útreikningarnir féllu')
    
    def testDateFilter(self):
        utkoma = launamidi.dateFilter("17.ágúst 2009")
        self.assertEqual(self.arrDagsetning, utkoma, 'DateFilter testið féll')
        
    def testManudurSemNumer(self):
        utkoma = launamidi.manudurSemNumer("ágúst")
        self.assertEqual(8, utkoma, 'Fall sem skilar númer mánuðs féll')

if __name__ == '__main__': unittest.main()
