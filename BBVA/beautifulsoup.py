import urllib2;
import re;
import csv;
import Lineup;
from bs4 import BeautifulSoup


def existDate(dateList, newDate):
    result = "true";
    for i in range(len(dateList)):
        #print "list: ", dateList[i];
        #print "new:  ", newDate;
        if cmp(newDate, dateList[i]) == 0:
            result = "true";
            break;
        else:
            result = "false"; 
    #print "result: ", result;
    return result;

def extractDate(htmlTable):
    dateLine = htmlTable.find_all("tr", "stathead");
    return dateLine[0].string;

def myfunction(text):
    # try:
    #     text = unicode(text);
    #     text = text.encode("ascii",'ignore');
    # except TypeError:
    # return text;
    text = unicode(text);
    text = text.encode("ascii",'ignore');
    return text;

def extractHome(htmlTable):
    home = [];
    dateLine = htmlTable.find_all("td", align="right");
    #print dateLine;
    for a in dateLine:
        homeLine = a.find_all("a");
        if (homeLine):
            home_name = homeLine[0].string;
            home_name = myfunction(home_name);
            home.append(home_name);
            #print homeLine[0].string;
    return home;

def extractScore(htmlTable):
    scores = [];
    scoreLine = htmlTable.find_all("td", align="center");
    #print scoreLine;
    for a in scoreLine:
        score = a.find_all("a");
        if (score):
            scores.append(score[0].string);
    return scores;
    
def extractLinks(htmlTable):
    links = [];
    linksLine = htmlTable.find_all("td", align="center");
    #print linksLine;
    for a in linksLine:
        link = a.find_all("a");
        if (link):
            links.append(link[0].get('href'));
    return links;

def extractAway(htmlTable):
    aways = [];
    awaysLine = htmlTable.find_all("td", align="left");
    #print awaysLine;
    for a in awaysLine:
        away = a.find_all("a");
        if (away):
            away_name = away[0].string;
            away_name = myfunction(away_name);
            aways.append(away_name);
    return aways;

def writeCSV_init():
    fileWriter = csv.writer(open('score.csv', 'a'));
    fileWriter.writerow(['Home', 'Score', 'Away']);

def writeCSV(bDate, bHome, bScore, bAway):
    fileWriter = csv.writer(open('score.csv', 'ab'));
    # for i in bHome:
    #     for a in bScore:
    #         for b in bAway:
    #             fileWriter.writerow([i] + [a] + [b]);
    for i in range(len(bHome)):
        fileWriter.writerow([bHome[i]] + [bScore[i]] + [bAway[i]]);

page = 20120815;
#writeCSV_init();
battleDate = [];
battleDate.append('Friday, August 17, 2012');
while page <= 20130528:
    page = str(page);
    print page;
    try:
        #response = urllib2.urlopen('http://espnfc.com/results/_/date/'+page+'/league/eng.1/english-premier-league?cc=5901');
        response = urllib2.urlopen('http://espnfc.com/results/_/date/'+page+'/league/esp.1/spanish-la-liga?cc=5901');
        #response = urllib2.urlopen('http://espnfc.com/results/_/date/2012916/league/eng.1/english-premier-league?cc=5901');
        html = response.read();
    except urllib2.HTTPError, error:
        html = error.read();
    soup = BeautifulSoup(html);
    battleHome = [];
    battleScore = [];
    battleLinks = [];
    battleAway = [];
    homePosition = [];
    homeID = [];
    homeName = [];
    awayPosition = [];
    awayID = [];
    awayName = [];
    #print soup.prettify();
    #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~";
    for a in soup.find_all('table'):
        #print a, "\n";
        #print "Date: ", extractDate(a);
        if existDate(battleDate, extractDate(a)) == "true":
            print "same\n";
        else: 
            battleDate.append(extractDate(a));
            battleHome = extractHome(a);
            #for i in range(len(battleHome)):
               #print "Home: ", battleHome[i];
            battleScore = extractScore(a);
            #for i in range(len(battleScore)):
            #    print "Score: ", battleScore[i];
            battleLinks = extractLinks(a);
            #for i in range(len(battleLinks)):
            #    print "Link: ", battleLinks[i];
            battleAway = extractAway(a);
            #for i in range(len(battleAway)):
            #    print "Away: ", battleAway[i];

            #writeCSV(battleDate, battleHome, battleScore, battleAway);
            Lineup.main_1(battleLinks, battleHome, battleAway);
    page = int(page);
    page = page + 15;
    # num = page % 100;
    # numMonth = page % 10000;
    # if num >= 40:
    #     page = page - 48 + 100;
    # if numMonth >= 1300:
    #     page = page - 1308 + 10000;
    # except urllib2.HTTPError, error:
    #     print "error\n", page;
    #     html = error.read();
    #     soup = BeautifulSoup(html);
    #     print(soup.prettify());
    #     page = int(page);
    #     page = page + 16;
    #     num = page % 100;
    #     numMonth = page % 10000;
    #     if num >= 40:
    #         page = page - 48 + 100;
    #     if numMonth >= 1300:
    #         page = page - 1308 + 10000;
    #     contents = error.read();
    #     continue;
