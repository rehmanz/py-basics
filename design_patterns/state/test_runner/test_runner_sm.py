'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" TestRunnerStateMachine Class """
class TestRunnerStateMachine:
    def __init__(self):
        pass
    
""" Unit Tests """
class TestRunnerStateMachineUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def TestRunnerStateMachineUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(TestRunnerStateMachineUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='TestRunnerStateMachineUnitTestRunner',
                  verbosity=2)

