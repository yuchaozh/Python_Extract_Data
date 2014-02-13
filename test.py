import urllib2;
import re;
import csv;
import Lineup;
from bs4 import BeautifulSoup


page = 20120916;
page = str(page);
response = urllib2.urlopen('http://espnfc.com/results/_/date/'+page+'/league/eng.1/english-premier-league?cc=5901');
html = response.read();
soup = BeautifulSoup(html);
print(soup.prettify());