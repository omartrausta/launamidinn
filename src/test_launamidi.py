# encoding: utf-8
import unittest, launamidi

class LaunamidarTestCase(unittest.TestCase):    
    stimplanir = [("17.ágúst 2009", ("09:00", "10:00"))]
    taxtar = [("dv", ("09:00", "17:00"), [0, 1, 2, 3, 4]),
              ("ev", ("17:00", "19:00"), [0, 1, 2, 3, 4]),
              ("nv", ("00:00", "09:00"), [0, 1, 2, 3, 4]),
              ("yv", ("19:00", "23:59"), [0, 1, 2, 3, 4]),
              ("nv", ("00:00", "23:59"), [5, 6])]
    
    stimplanir2 = [("16.ágúst 2009", ("07:00", "15:00")),
                   ("17.ágúst 2009", ("10:00", "20:00")),
                   ("19.ágúst 2009", ("13:00", "23:00")),
                   ("20.ágúst 2009", ("05:00", "06:00"))]
    
    nidurstada = {'dv': 1.0,'ev': 0.0,'nv': 0.0,'yv': 0.0}
    nidurstada2 = {'dv': 11.0,'ev': 4.0,'nv': 9.0,'yv': 5.0}
    arrDagsetning = ['17', 'ágúst', '2009']
       
    def testVinna(self):
        utkoma = launamidi.vinna(self.stimplanir, self.taxtar)
        self.assertEqual(self.nidurstada,utkoma)
    
    def test3Innstimplanir(self):
        utkoma = launamidi.vinna(self.stimplanir2, self.taxtar)
        self.assertEqual(self.nidurstada2,utkoma)
    
    def testDateFilter(self):
        utkoma = launamidi.dateFilter("17.ágúst 2009")
        self.assertEqual(self.arrDagsetning, utkoma, 'DateFilter testið féll')
        
    def testManudurSemNumer(self):
        utkoma = launamidi.manudurSemNumer("ágúst")
        self.assertEqual(8, utkoma, 'Fall sem skilar númer mánuðs féll')

if __name__ == '__main__': unittest.main()
