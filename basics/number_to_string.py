'''
Created on Sep 26, 2015

@author: zrehman
'''
import unittest

letters_d = {
    1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine',
    10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen',
    20 : 'twenty', 30 : 'thirty', 40 : 'fourty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy', 80 : 'eighty', 90 : 'ninety',
    100 : 'one hundred',
    1000 : 'one thousand'
}


base_scale = {
    3 : 'hundred', 4 : 'thousand', 7 : 'million', 8: 'one hundred million', 10 : 'billion', 13 : 'trillion'
}

def get_base_scale(num):
    l = len(str(num))
    base = ''
    if l in base_scale.keys():
        return base_scale[l]

def int_to_words(num):
    print('------------')
    print(str(num))
    print('============')

    s = str(num)
    l = len(s)-1
    letter = ''
    char_counter = 0
    for i in xrange(0,l,3):

        letter += ''
        print("index=%s, number=%s, letter=%s, base_scale=%s" %(i, s[i:i+3], letter, get_base_scale(s[char_counter:])))
        char_counter = char_counter + 3

    remainder_s = s[char_counter:]
    if remainder_s:
        print("remainder_s=%s, char_counter: %s, len=%s, base_scale=%s -> %s"
              %(remainder_s, char_counter, l, get_base_scale(s[char_counter:]), remainder_s))
    print('')

def letters(n):
    s = str(n)
    l = len(s)-1
    for i in range(0, len(s)):
        print(s[i])

""" Unit Tests """
class NumberToStringUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        pass

    def test_small_numbers(self):
        letters(1934)
        #for num in [1, 10, 100, 1123456, 1000000000, 1000000000000, 1000000000000000]:
        #    int_to_words(num)

    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def NumberToStringUnitTestRunner():
    tests = ['test_small_numbers']

    return unittest.TestSuite(map(NumberToStringUnitTest, tests))

if __name__ == "__main__":
    unittest.main(defaultTest='NumberToString', verbosity=2)
