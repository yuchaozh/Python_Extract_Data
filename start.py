import urllib2;
import re;
response = urllib2.urlopen('http://espnfc.com/results/_/date/20120818/league/eng.1/english-premier-league?cc=5901');
html = response.read();
#print html
findDate = re.findall('<tr class="stathead"><td colspan="7">(.*)</td></tr>', html);
if (findDate):
    #print "start date: ", findDate;
    #fDate = findDate.group();
    print "start date: ", findDate;
findHome = re.findall('<td align="right"><a href=.*>(.*)</a></td>', html);
if (findHome):
    #print "start date: ", findHome;
    #fHome = findHome.group();
    print "home: ", findHome;
findScore = re.findall('<td align="center"><a href=.*>(.*)</a></td>', html);
if (findScore):
    #print "start date: ", findScore;
    #fScore = findScore.group();
    print "  ", findScore, "  ";
findAway = re.findall('<td align="left"><a href=.*>(.*)</a></td>', html);
if (findAway):
    #print "start date: ", findAway;
    #fAway = findAway.group();
    print "away: ", findAway;
#print "home: ", findHome, "  ", findScore, "  ", "away:", findAway;