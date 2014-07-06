'''
Created on Jul 5, 2014

@author: zrehman
'''
import unittest
import json

from collections import OrderedDict

"""SymbolTable class stores a key-value pair into a table. Given a key, the
corresponding value is returned. Both keys and values are stored in two 
separate lists.
"""
class SymbolTable:
    def __init__(self):
        self.table = OrderedDict()
    
    """Put key-value pair into the table (remove key from table for null value)
    
    :param key: The key
    :param value: The value to be stored
    """
    def put(self, key, val):
        self.table[key] = val
    
    """Return value paired with key (null if key is absent)
    
    :param key: The key
    """
    def get(self, key):
        if key in self.table:
            return self.table[key]
    
    """Remove key and it's value from the table
    
    :param key: The key
    """
    def delete(self, key):
        if key in self.table:
            del self.table[key]
    
    """Return True if there is a value paired with key, false otherwise
    
    :param key: The key
    """
    def contains(self, key):
        if key in self.table:
            return True
        else:
            return False
    
    """Return if the table is empty
    """
    def is_empty(self):
        return len(self.table) == 0
    
    """Return the table size(i.e. number of key-value pairs in the table)
    """
    def size(self):
        return len(self.table)
    
    """Return all the keys in the table as a list
    """
    def keys(self):
        return self.table.keys()
    
    """ Private Methods """
    def __str__(self):
        out = "\n"
        out += "%s\n" %(json.dumps(self.table, indent=4, 
                                   separators=(',',':')))
        return out
    
""" Unit Tests """
class SymbolTableUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.st = SymbolTable()
        
    
    def test_put(self):
        st = OrderedDict()
        keys_l = ['S', 'E', 'A', 'H', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        vals_l  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(0, len(keys_l)):
            self.st.put(keys_l[i], vals_l[i])
    
    def test_print(self):
        print self.st
    
    def test_get(self):
        self.assertEqual(self.st.get('A'), 6)
        self.assertEqual(self.st.get('ZZ'), None)
    
    def test_contains(self):
        self.assertEqual(self.st.contains('X'), True)
        self.assertEqual(self.st.contains('XX'), False)
    
    def test_delete(self):
        self.assertEqual(self.st.contains('E'), True)
        self.st.delete('E')
        self.assertEqual(self.st.contains('E'), False)
    
    def test_is_empty(self):
        self.assertEqual(self.st.is_empty(), False)
    
    def test_get_keys(self):
        self.assertEqual(self.st.keys(), ['S', 'A', 'H', 'X', 'M', 'P', 'L'])
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def SymbolTableUnitTestRunner():
    tests = ['test_put',
             'test_print',
             'test_get',
             'test_contains',
             'test_delete',
             'test_is_empty',
             'test_get_keys']
    
    return unittest.TestSuite(map(SymbolTableUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='SymbolTableUnitTestRunner', verbosity=2)
