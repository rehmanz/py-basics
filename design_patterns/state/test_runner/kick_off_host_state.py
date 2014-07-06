'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" KickOffHostState Class """
class KickOffHostState:
    def __init__(self):
        pass
    
""" Unit Tests """
class KickOffHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def KickOffHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(KickOffHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='KickOffHostStateUnitTestRunner',
                  verbosity=2)