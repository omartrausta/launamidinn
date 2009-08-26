# encoding: utf-8
import unittest, hvada_skrar_eru_staestar, os

class HvadaSkrarEruStaestarTestCase(unittest.TestCase):    
    numberOfFiles = 3
    
    path = os.getcwd() + os.sep + "py"
    
    # 
    expectedResult = [('/home/gunnl/dev/workspace/Verkefni1/src/py/medium_file', 12L), ('/home/gunnl/dev/workspace/Verkefni1/src/py/large_file', 84L), ('/home/gunnl/dev/workspace/Verkefni1/src/py/extra_large_file', 23346L)]
    
    def testDtstat(self):
        print self.path
        result = hvada_skrar_eru_staestar.dtstat(self.path, self.numberOfFiles)
        print result
        print self.expectedResult
        self.assertEqual(result, self.expectedResult, 'Test féll')
        
if __name__ == '__main__': unittest.main()
