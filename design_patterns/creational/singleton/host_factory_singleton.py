'''
Created on Jul 6, 2014

@author: zrehman
'''
import unittest

""" HostFactorySingleton Class """
class HostFactorySingleton(object):
    __instance = None
    def __new__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance = super(HostFactorySingleton, self).__new__(
                                    self, *args, **kwargs)
        return self.__instance
    
""" Unit Tests """
class HostFactorySingletonUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.instance1 = HostFactorySingleton()
        self.instance2 = HostFactorySingleton()
    
    def test_it(self):
        self.assertEqual(self.instance1, self.instance2)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def HostFactorySingletonUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(HostFactorySingletonUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='HostFactorySingletonUnitTestRunner',
                  verbosity=2)