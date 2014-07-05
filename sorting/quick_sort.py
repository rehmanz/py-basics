'''
Created on Jul 4, 2014

@author: zrehman
'''
import unittest

def quick_sort(l):
    pass

""" Unit Tests """
class QuickSortUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_small_array(self):
        l = k = [9, 2, 4, 3]
        k.sort()
        self.assertEqual(quick_sort(l), k)
    
    def test_one_element_aray(self):
        l = k = [10]
        k.sort()
        self.assertEqual(quick_sort(l), k)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def QuickSortUnitTestRunner():
    tests = ['test_small_list',
             'test_one_element_list',
             'test_empty_list']
    
    return unittest.TestSuite(map(QuickSortUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='QuickSortUnitTestRunner', verbosity=2)
