# encoding: utf-8
import unittest, combinations, os

class combinationsTestCase(unittest.TestCase):    
    litir=["gulur","rauður","grænn","blár","svartur","hvítur","fjólublár"]
    expected=[('gulur', 'rauður'), ('gulur', 'grænn'), ('gulur', 'blár'), ('gulur', 'svartur'), ('gulur', 'hvítur'), ('gulur', 'fjólublár'), ('rauður', 'grænn'), ('rauður', 'blár'), ('rauður', 'svartur'), ('rauður', 'hvítur'), ('rauður', 'fjólublár'), ('grænn', 'blár'), ('grænn', 'svartur'), ('grænn', 'hvítur'), ('grænn', 'fjólublár'), ('blár', 'svartur'), ('blár', 'hvítur'), ('blár', 'fjólublár'), ('svartur', 'hvítur'), ('svartur', 'fjólublár'), ('hvítur', 'fjólublár')]
    number=2
     
    def testWork(self):
        result = combinations.work(self.litir, self.number)
        print result
        self.assertEqual(result, self.expected, 'Test féll')
        
if __name__ == '__main__': unittest.main()
