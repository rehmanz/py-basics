'''
Created on Jul 5, 2014

@author: zrehman
'''
import unittest

from flys import Flys, ItFlys, ItFlysSuperFast, CantFly

class Animal:
    def __init__(self, name):
        try:
            self.name  = name
        except Exception as e:
            raise ValueError('AnimalExceptionError - Constructor failed: %s'
                             %(e))
    
    def try_to_fly(self):
        return self.fly_o.fly()
    
    def set_flying_ability(self, fly_o):
        self.fly_o = fly_o

    """ Public Methods """
    def get_name(self):
        return self.name

class Bird(Animal):
    def __init__(self, name):
        Animal.__init__(self, name=name)
        self.fly_o = Flys(context=ItFlys)

class SuperFastBird(Bird):
    def __init__(self, name):
        Bird.__init__(self, name=name)
        self.fly_o = Flys(context=ItFlysSuperFast)

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name=name)
        self.fly_o = Flys(context=CantFly)
    
""" Unit Tests """
class AnimalUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.bird_o = Bird('Tweety')
        self.dog_o  = Dog('Hooch')
        self.eagle_o = SuperFastBird('Eagle')
    
    def test_fly(self):
        self.assertEqual(self.bird_o.try_to_fly(), 'Soaring high!')
        self.assertEqual(self.eagle_o.try_to_fly(), 'Flying like an eagle!')
        self.assertEqual(self.dog_o.try_to_fly(), 'Can\'t fly')
    
    def test_dog_flies_now(self):
        self.dog_o.set_flying_ability(Flys(context=ItFlys))
        self.assertEqual(self.dog_o.try_to_fly(), 'Soaring high!')
        
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def AnimalUnitTestRunner():
    tests = ['test_fly',
             'test_dog_flies_now']
    
    return unittest.TestSuite(map(AnimalUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='AnimalUnitTestRunner', verbosity=2)
