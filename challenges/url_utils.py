'''
Created on Jul 4, 2014

@author: zrehman
'''
import unittest

def hash_my_url(url):
    """Return a number between 1 and 1000

    url -- the website address
    """
    # Convert each char in url to an int and store in int_val_l list
    int_val_l = map(ord, url)

    # Sum up all the integer element and get a value less than 1000s
    return (reduce(lambda x, y: x+y, int_val_l))%1000

""" Unit Tests """
class FrequenceCounterUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass
    
    def test_it(self):
        print hash_my_url('www.yahoo.com')
        print hash_my_url('sports.yahoo.com')
        print hash_my_url('www.google.com')
        print hash_my_url('www.mysite.tv')
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def FrequenceCounterUnitTestRunner():
    tests = ['test_it']
    
    return unittest.TestSuite(map(FrequenceCounterUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='FrequenceCounterUnitTestRunner', verbosity=2)
