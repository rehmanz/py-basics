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

    python url_crawler.py filename
    
    positional arguments:
        filename    file containing timestamp and url data, i.e. "1407564301|www.kings.com"

    optional arguments:
        -h, --help  show this help message and exit

Complexity Analysis
--------------------
- Each record is stored in a nested hash with time stamp key as the top level and url under the applicable time stamp key. File is read in linear time (i.e. O(N)) while records are created in contant time.
- A report is generated in linear time (i.e. O(N)). Both time stamp and url structures are stored in a list (i.e. O(N)). They are, then, sorted using python's built in sort algorith (i.e. O(N log N)).

Exception Handling
-------------------
- File exceptions are handled
- Input data is validated before a record is created. If the data is malformed, it is skipped with a warning message