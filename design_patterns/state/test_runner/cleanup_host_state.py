'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" CleanupHostState Class """
class CleanupHostState:
    def __init__(self):
        pass
    
""" Unit Tests """
class CleanupHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def CleanupHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(CleanupHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='CleanupHostStateUnitTestRunner',
                  verbosity=2)