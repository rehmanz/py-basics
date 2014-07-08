'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" DictionaryComparison Class """
class DictionaryComparison:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
       
        if (not isinstance(self.d1, dict)) and (not isinstance(self.d2, dict)):
            raise ValueError('Type mismatch: d1 and d2 must be dict type')
    
    def __contains__(self):
        return False
    
""" Unit Tests """
class DictionaryComparisonUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.d1 = {'A' : 1}
        self.d2 = {'B' : 2}
        self.d = DictionaryComparison(self.d1, self.d2)
    
    def test_ne(self):
        self.assertFalse(self.d1 == self.d2)
    
    def test_eq(self):
        self.assertTrue(self.d1 == self.d1)
    
    def test_in(self):
        print 
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def DictionaryComparisonUnitTestRunner():
    tests = ['test_ne',
             'test_eq',
             'test_in']
    
    return unittest.TestSuite(map(DictionaryComparisonUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='DictionaryComparisonUnitTestRunner',
                  verbosity=2)
