import urllib2;
import re;
import csv;
#import Lineup;
from bs4 import BeautifulSoup

def myfunction(text):
    # try:
    #     text = unicode(text);
    #     text = text.encode("ascii",'ignore');
    # except TypeError:
    # return text;
    text = unicode(text);
    text = text.encode("ascii",'ignore');
    return text;

file = open('Granada Club de Futbol.txt', 'a');
try:
    response = urllib2.urlopen('http://sofifa.com/en/14w/t/110832-granada-club-de-futbol');
    html = response.read();
except urllib2.HTTPError, error:
    html = error.read();

soup = BeautifulSoup(html);
for a in soup.find_all('tr'):
    b = a.find_all('td');
    # if b is not null
    if b:
        player_NO = b[1].string;
        print "no: ";
        print player_NO;
        player_name = b[6].string;
        player_name = myfunction(player_name);
        print "name: ";
        print player_name;
        ovr_tag = b[5].find_all('span');
        player_ovr = ovr_tag[0].string;
        print "ovr: ";
        print player_ovr;
        file.write(player_NO+","+player_name+","+player_ovr+'\n');
file.close();
