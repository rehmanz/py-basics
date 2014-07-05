'''
Created on Jul 4, 2014

@author: zrehman
'''
import unittest

def merge(left, right):
    result = []
    i = j = 0
    
    # Conquer
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    
    # Divide
    middle  = len(l) / 2
    left    = merge_sort(l[:middle])
    right   = merge_sort(l[middle:])
    
    return merge(left, right)

""" Unit Tests """
class MergeSortUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_small_array(self):
        l = k = [9, 2, 4, 3]
        k.sort()
        self.assertEqual(merge_sort(l), k)
    
    def test_one_element_aray(self):
        l = k = [10]
        k.sort()
        self.assertEqual(merge_sort(l), k)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def MergeSortUnitTestRunner():
    tests = ['test_small_list',
             'test_one_element_list',
             'test_empty_list']
    
    return unittest.TestSuite(map(MergeSortUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='MergeSortUnitTestRunner', verbosity=2)
