# encoding: utf-8
import unittest, combinations, os

class combinationsTestCase(unittest.TestCase):    
    litir=["gulur","rauður","grænn","blár","svartur","hvítur","fjólublár"]
    number=2
     
    def testMoguleikar(self):
        result = combinations.moguleikar(self.litir, self.number)
        print result
        #self.assertEqual(result, self.expectedResult, 'Test féll')
        
if __name__ == '__main__': unittest.main()
