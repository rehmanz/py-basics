URL Crawler
============
UrlCrawler parses crawler log and generates a report containing URL hit counts for each day

Introduction
-------------
Given an input file, 

- each line consists of a timestamp (unix epoch in seconds) and a url separated by ‘|’ symbol
- entries are not in any chronological order. 

a report is generated containing
- number of times each url is visited in a day
- sorted by the url hit count for each url entry

Usage
------
.. code :: python

    usage: url_crawler.py [-h] filename
    
    positional arguments:
        filename    file containing timestamp and url data, i.e. "1407564301|www.kings.com"

    optional arguments:
        -h, --help  show this help message and exit