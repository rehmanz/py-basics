'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

from computer_components import BootStrap, SetupNetworking

""" ComputerFacade Class """
class ComputerFacade:
    def __init__(self):
        self.bootstrap_o = BootStrap()
        self.network_o   = SetupNetworking()
    
    def start(self):
        self.bootstrap_o.start()
        self.network_o.setup()
        return True
    
""" Unit Tests """
class ComputerFacadeUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.computer_o = ComputerFacade()
    
    def test_it(self):
        self.assertTrue(self.computer_o.start())
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def ComputerFacadeUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(ComputerFacadeUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='ComputerFacadeUnitTestRunner',
                  verbosity=2)
