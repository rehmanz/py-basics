URL Crawler
============
UrlCrawler parses crawler log and generates a report containing URL hit counts for each day

Introduction
-------------
Given an input file, 

- each line consists of a timestamp (unix epoch in seconds) and a url separated by ‘|’ symbol
- entries are not in any chronological order. 

this program generate a report containing
- number of times each url is visited in a day
- sorted by the url hit count for each url entry