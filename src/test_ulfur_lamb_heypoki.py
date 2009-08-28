# encoding: utf-8
import unittest, ulfur_lamb_heypoki

class UlfurLambHeypokiTestCase(unittest.TestCase):
    upphafsstada = ["bulh", ""]
    expectedStada = True
    
    def testVinna(self):
        utkoma = ulfur_lamb_heypoki.keyra(self.upphafsstada)
        self.assertEqual(self.expectedStada, utkoma)

if __name__ == '__main__': unittest.main()