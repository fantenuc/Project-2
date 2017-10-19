import unittest
import requests
import re
from bs4 import BeautifulSoup


def find_urls(s):
    url = re.findall('http[s]?://[A-Za-z0-9]+\.\S{2,}', s)

    print(url)
    return url

find_urls('http://bbc.co.uk')
find_urls('https://www.gmail.com')
find_urls('https://gmail.com')
find_urls('gmail.gov')
find_urls('http://nationalparkservice.gov/pictures/badlands')
find_urls('http://bbc.c')
find_urls('http://bbc.c hey')
find_urls('http://bbc.com.us.h')