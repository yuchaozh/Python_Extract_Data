import urllib2;
import re;
import csv;
import codecs;
import sys;
from bs4 import BeautifulSoup

def extractPosition(table):
    #print table, "\n";
    positions = [];
    position = table.find_all("td", "first");
    for a in position:
        #print a, "\n";
        positions.append(a.string);
    return positions;

def extractID(table):
    #print table, "\n";
    ids = [];
    member = table.find_all("td", "first");
    #print member;
    #for i in range (0, 11):
    for a in member:
        #print member[i];
        #cont = member[i].next_sibling.next_sibling.string;
        #print cont;
        ids.append(a.next_sibling.next_sibling.string);
        #print a.next_sibling.next_sibling.string;
    return ids;

def myfunction(text):
    # try:
    #     text = unicode(text);
    #     text = text.encode("ascii",'ignore');
    # except TypeError:
    # return text;
    text = unicode(text);
    text = text.encode("ascii",'ignore');
    return text;

def extractName(table):
    #print table, "\n"
    names = [];
    member = table.find_all("td", "first");
    for a in member:
        isoName =  a.next_sibling.next_sibling.next_sibling.next_sibling.find_all("a")[0].string;
        #uName = unicode (isoName, "ISO-8859-1");
        #name = uName.encode ("ascii");
        name = myfunction(isoName);
        #print "type: ", type(name);
        names.append(name);
    return names;

def main_2(pageURL, homeName1, awayName1):
    #sys.getdefaultencoding();
    file = open('lineup.txt', 'a');
    #page = 'http://espnfc.com/us/en/gamecast/statistics/id/345817/statistics.html?soccernet=true&cc=5901';
    #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
    #print pageURL, "\n";
    print "\n";
    file.write('\n');
    response = urllib2.urlopen(pageURL);
    html = response.read();
    homePosition = [];
    homeID = [];
    homeName = [];
    awayPosition = [];
    awayID = [];
    awayName = [];
    parse = BeautifulSoup(html);
    #print parse.prettify();
    tables = parse.find_all("section", "mod-container");
    homeTable = tables[3];
    awayTable = tables[4];
    homePosition = extractPosition(homeTable);
    homeID = extractID(homeTable);
    homeName = extractName(homeTable);
    awayPosition = extractPosition(awayTable);
    awayID = extractID(awayTable);
    awayName = extractName(awayTable);
    #print "\n";
    print homeName1, "  VS.  ", awayName1, ":";
    file.write(homeName1+"  VS.  "+awayName1+":"+'\n');
    for i in range (0, 11):
        print homePosition[i],",", homeID[i],",", homeName[i];
        file.write(homePosition[i]+","+homeID[i]+","+homeName[i]+'\n');
    #print "!!!!!!~~~~~~~~~~~~~~";
    print "--------------------------";
    file.write("--------------------------\n");
    #print awayName1, ":";
    for i in range (0, 11):
        print awayPosition[i],",", awayID[i],",", awayName[i];
        file.write(awayPosition[i]+","+awayID[i]+","+awayName[i]+'\n');
    file.close();

def main_1(pageUrl, home, away):
    #print pageUrl;
    for i in range(len(pageUrl)):
        #print pageUrl[i];
        #pageID = pageUrl[i][33:39];
        pageID = pageUrl[i].split('/');
        pageID = pageID[6];
        print pageID;
        pageID = str(pageID);
        newUrl = 'http://espnfc.com/us/en/gamecast/statistics/id/'+pageID+'/statistics.html?soccernet=true&cc=5901';
        #newUrl = 'http://espnfc.com/us/en/gamecast/statistics/id/'+pageID+'/statistics.html?soccernet=true&cc=5901';
        #print newUrl;
        main_2(newUrl, home[i], away[i]);
    