# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:12:30 2020

@author: Redouane Hemi
"""
# Downloading Airfoils from  
# University of Illinois at Urbana-Champaign Database: 

##Beautiful Soup is a Python package for parsing HTML and XML documents.
##It creates a parse tree for parsed pages that can be used to extract data from HTML
from bs4 import BeautifulSoup
#urllib is a Python module for fetching URLs
import urllib
# import regular expression
import re

url_database1="https://m-selig.ae.illinois.edu/ads/coord_database.html"
html = urllib.request.urlopen(url_database1)			
beautifulSoup = BeautifulSoup(html,'lxml')
baseLink = "https://m-selig.ae.illinois.edu/ads/"

#download aerofoil files .dat format for flying wing purpose 
links= beautifulSoup.find_all('a',attrs={'href': re.compile('\.dat', re.IGNORECASE)})
for link in links:
    if re.search("flying wing",link.next_element.next_element):
        urllib.request.urlretrieve(baseLink+link.get('href'), filename=link.get('href').rsplit('/',1)[-1].upper())	
        print(link.get('href').rsplit('/',1)[-1].upper())	
print("... END")															
