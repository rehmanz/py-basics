'''
Created on Jul 5, 2014

@author: zrehman
'''
import unittest
import types

""" Flys Strategy Class """
class Flys(object):
    def __init__(self, context=None):
        self.action = context()
    
    def set_flying_ability(self, context):
        self.action = context()
    
    def fly(self):
        return self.action.execute()

""" Concrete Strategies """
class ItFlys(object):
    def execute(self):
        return 'Soaring high!'

class ItFlysSuperFast(object):
    def execute(self):
        return 'Flying like an eagle!'

class CantFly(object):
    def execute(self):
        return 'Can\'t fly'
    
""" Unit Tests """
class FlyStrategyUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.fly_o = Flys(context=ItFlys)
    
    def test_fly(self):
        self.assertEqual(self.fly_o.fly(), 'Soaring high!')
    
    def test_set_flying_ability(self):
        self.fly_o.set_flying_ability(context=CantFly)
        self.assertEqual(self.fly_o.fly(), 'Can\'t fly')
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def FlyStrategyUnitTestRunner():
    tests = ['test_fly',
             'test_set_flying_ability']
    
    return unittest.TestSuite(map(FlyStrategyUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='FlyStrategyUnitTestRunner', verbosity=2)
