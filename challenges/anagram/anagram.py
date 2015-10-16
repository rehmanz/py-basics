__author__ = 'zile'

import re
import json
import time
import unittest
import logging
import argparse

from datetime import date

LOGGER = logging.getLogger()

class Anagram():
    """
    Anagram class parses crawler log and generates a report containing URL hit counts for each day
    """

    def __init__(self, filename):
        """
        :param filename: lines contain a timestamp and a url separated by "|"
        """
        self.filename = filename

    def read(self):
        """Read the file and generate report to stdout
        :return: None
        """
        self.record_d = {}
        self.__read_file()

    def __input_data_ok(self, line=None):
        """Checks if input data is ok
        :line: line containing the anagram data
        :return: True for success, False otherwise
        """
        return True

    def __get_word_d(self, word):
        """Returns dictionary consisting the individual char count
        :word: word
        :return: Dictionary
        """
        d = {}
        for c in word:
            if not c in d:
                d[c] = 1
            else:
                d[c] += 1
        return d

    def __check_anagrams(self, w1, w2):
        """Checks if w1 and w2 are anagrams
        :w1: first word
        :w2: second word
        :return: True for success, False otherwise
        """
        d1 = self.__get_word_d(w1)
        d2 = self.__get_word_d(w2)

        return d1 == d2

    def __read_file(self):
        """Read the file and create a record for each line
        :return: True for success, False otherwise
        """
        try:
            with open(self.filename) as fh:
                for line in fh:
                    if self.__input_data_ok(line.strip()):
                        print(line.strip().split("\t"))
                        first_word, second_word = line.strip().split("\t")
                        #LOGGER.debug("%s %s" %(first_word, second_word))
                        if self.__check_anagrams(first_word, second_word):
                            LOGGER.info("%s %s == True" %(first_word, second_word))
                        else:
                            LOGGER.info("%s %s == False" %(first_word, second_word))
                    else:
                       LOGGER.warn("Anagram Malformed Line (Skipping): \"%s\"" %line)

            LOGGER.debug(json.dumps(self.record_d, indent=4, separators=(',',':')))
            return True

        except Exception as e:
            LOGGER.error("Anagram File Read Exception: %s" %(e))
            return False


""" Unit Tests """
class AnagramUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logging.basicConfig(level=logging.INFO)

    #@unittest.skip("skipping")
    def test_small_set(self):
        Anagram(filename="data/small_set.txt").read()

    @unittest.skip("skipping")
    def test_corner_cases(self):
        pass
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def AnagramUnitTestRunner():
    tests = ['test_small_set',
             'test_corner_cases']
    
    return unittest.TestSuite(map(AnagramUnitTest, tests))

if __name__ == "__main__":
    """ Default log level """
    logging.basicConfig(level=logging.INFO)

    """ Command Parser """
    parser = argparse.ArgumentParser()

    """ Required Parameters Definition """
    parser.add_argument("filename",
                        help="file containing anagram data, i.e. \"maria    riama\"")

    """ Parse Arguments """
    args = parser.parse_args()

    """ Process Arguments """
    filename = args.filename

    try:
        Anagram(filename=filename).read()
    except Exception as e:
        LOGGER.error("Main Program Exception: %s" %e)
