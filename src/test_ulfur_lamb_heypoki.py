# encoding: utf-8
import unittest, ulfur_lamb_heypoki

class UlfurLambHeypokiTestCase(unittest.TestCase):
    def testVinna(self):
        vandi = ["bulh", ""]
        print vandi
        print ulfur_lamb_heypoki.logleg_stada(vandi)
        vandi = ulfur_lamb_heypoki.haegri(vandi, "u")
        vandi = ulfur_lamb_heypoki.haegri(vandi, "b")
        print vandi
        print ulfur_lamb_heypoki.logleg_stada(vandi)

if __name__ == '__main__': unittest.main()