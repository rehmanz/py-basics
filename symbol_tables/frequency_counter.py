'''
Created on Jul 5, 2014

@author: zrehman
'''
import unittest

from symbol_table import SymbolTable

""" FrequenceCounter Class """
class FrequenceCounter(SymbolTable):
    def __init__(self):
        SymbolTable.__init__(self)
    
    """Put key-value pair into the table (remove key from table for null value)
    
    :param key: The key
    """
    def put(self, key):
        self.table[key] = 0
    
""" Unit Tests """
class FrequenceCounterUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.st = FrequenceCounter()
        
        content = ''
        with open('data/book.txt') as f:
            content = f.readlines()
        
        freq = {}
        for line in content:
            for word in line.split(' '):
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

        word_l = ['her', 'him']
        for word in word_l:
            if word in freq:
                print("Word: %s, Count=%s" %(word, freq[word]))

        
    def test_put(self):
        pass
        #elf.st.put(key)
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def FrequenceCounterUnitTestRunner():
    tests = ['test_put']
    
    return unittest.TestSuite(map(FrequenceCounterUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='FrequenceCounterUnitTestRunner', verbosity=2)
