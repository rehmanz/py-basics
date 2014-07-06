'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" ConfigureHostState Class """
class ConfigureHostState:
    def __init__(self):
        pass
    
""" Unit Tests """
class ConfigureHostStateUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def ConfigureHostStateUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(ConfigureHostStateUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='ConfigureHostStateUnitTestRunner',
                  verbosity=2)