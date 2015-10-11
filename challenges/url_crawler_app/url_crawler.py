__author__ = 'zile'

import re
import json
import time
import unittest
import logging
import argparse

LOGGER = logging.getLogger()

class UrlCrawler():
    """
    UrlCrawler class parses crawler log and generates a report containing URL hit counts for each day
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
        if self.__read_file():
            self.__print_report()

    def __print_report(self):
        """Print report
        :return: None
        """
        self.report = ""
        self.report += "=====================================================================\n"
        self.report += "Input File: %s\n" %(self.filename)
        self.report += "---------------------------------------------------------------------\n"

        # create a sorted timestamp list
        timestamp_l = []
        for timestamp in self.record_d:
            timestamp_l.append(timestamp)
        timestamp_l.sort()

        for timestamp in timestamp_l:
            self.report += "%s\n" %(timestamp)
            LOGGER.debug(timestamp)

            # convert url record for this time stamp into list of tuples
            url_list_of_tuples = []
            for url in self.record_d[timestamp]:
                url_list_of_tuples.append((url, self.record_d[timestamp][url]))

            # sort based on the url frequency count, O(N log N)
            url_list_of_tuples.sort(key=lambda x: x[1], reverse=True)
            LOGGER.debug(url_list_of_tuples)

            for url_t in url_list_of_tuples:
                self.report += "%s %d\n" %(url_t[0], url_t[1])

        LOGGER.info("\n%s\n\n\n" %self.report)

    def __create_record(self, timestamp, url):
        """Inserts timestamp, url and url hit count in a nested dictionary structure
        :timestamp: timestamp
        :url: URL
        :return: None
        """
        if not timestamp in self.record_d.keys():
            self.record_d[timestamp] = {}

        # increment url count
        if not url in self.record_d[timestamp].keys():
            self.record_d[timestamp][url] = 1
        else:
            self.record_d[timestamp][url] += 1

    def __input_data_ok(self, line=None):
        """Checks if input data is ok
        :return: True for success, False otherwise
        """
        # valid pattern: 1407478022|www.facebook.com
        valid_pattern = re.compile("\w{10}\|\w+")
        if (line) and (re.match(valid_pattern, line)):
            return True
        else:
            return False

    def __get_formatted_time(self, t):
        """Returns formatted time string
        :t: epoch time in seconds
        :return: date string in "MM/DD/YYYY GMT" format
        """
        return time.strftime('%m/%d/%Y GMT', time.localtime(int(t)))

    def __read_file(self):
        """Read the file and create a record for each line
        :return: True for success, False otherwise
        """
        try:
            line_counter = 1
            with open(self.filename) as fh:
                for line in fh:
                    line_counter += 1
                    if self.__input_data_ok(line.strip()):
                        timestamp, url = line.strip().split("|")
                        LOGGER.debug("%s %s" %(timestamp, url))
                        self.__create_record(self.__get_formatted_time(timestamp), url)
                    else:
                        LOGGER.warn("URLCrawler Malformed Line (Skipping): \"%s\"" %line)

            LOGGER.debug(json.dumps(self.record_d, indent=4, separators=(',',':')))
            return True

        except Exception as e:
            LOGGER.error("URLCrawler File Read Exception: %s" %(e))
            return False


""" Unit Tests """
class UrlCrawlerUnitTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        logging.basicConfig(level=logging.INFO)

    #@unittest.skip("skipping")
    def test_small_set(self):
       UrlCrawler(filename="data/small_set.txt").read()

    #@unittest.skip("skipping")
    def test_corner_cases(self):
       self.assertRaises(Exception, UrlCrawler(filename="data/non_existing_file").read())
       UrlCrawler(filename="data/invalid_set.txt").read()
       UrlCrawler(filename="data/mixed_set.txt").read()
    
    @classmethod
    def tearDownClass(self):
        pass

""" Unit Test Runner """
def UrlCrawlerUnitTestRunner():
    tests = ['test_small_set',
             'test_corner_cases']
    
    return unittest.TestSuite(map(UrlCrawlerUnitTest, tests))

if __name__ == "__main__":
    """ Default log level """
    logging.basicConfig(level=logging.INFO)

    """ Command Parser """
    parser = argparse.ArgumentParser()

    """ Required Parameters Definition """
    parser.add_argument("filename",
                        help="file containing timestamp and url data, i.e. \"1407564301|www.kings.com\"")

    """ Parse Arguments """
    args = parser.parse_args()

    """ Process Arguments """
    filename = args.filename

    try:
        UrlCrawler(filename=filename).read()
    except Exception as e:
        LOGGER.error("Main Program: %s" %e)
