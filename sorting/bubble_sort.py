'''
Created on Jul 4, 2014

@author: zrehman
'''
import unittest

def bubble_sort(l):
    exchanged = True
    iteration = 0
    n = len(l)

    while(exchanged):
        iteration += 1
        exchanged = False

        # Move the largest element to the end of the list
        for i in range(n-1):
            if l[i] > l[i+1]:
                exchanged = True
                l[i], l[i+1] = l[i+1], l[i]
        n -= 1   # Largest element already towards the end
    return l

""" Unit Tests """
class BubbleSortUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_small_list(self):
        l = k = [9, 2, 4, 3]
        k.sort()
        self.assertEqual(bubble_sort(l), k)
    
    def test_one_element_list(self):
        l = k = [10]
        k.sort()
        self.assertEqual(bubble_sort(l), k)
    
    def test_long_list(self):
        l = k = [90, 10, 2, 76, 17, 66, 57, 23, 57, 99]
        k.sort()
        self.assertEqual(bubble_sort(l), k)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def BubbleSortUnitTestRunner():
    tests = ['test_small_list',
             'test_one_element_list',
             'test_long_list']
    
    return unittest.TestSuite(map(BubbleSortUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='BubbleSortUnitTestRunner', verbosity=2)
