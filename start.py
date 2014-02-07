import urllib2;
import re;
response = urllib2.urlopen('http://espnfc.com/results/_/date/20120820/league/eng.1/english-premier-league?cc=5901');
html = response.read();
html1 = html;
p=re.compile("\s+")
html=re.sub(p,'',html)
print html;
print html1;
print "~~~~~~~~~~~~~~~~~";

def extractTable(wholeHtml):
    findData = re.findall('<tableclass="tablehead"cellpadding="3"cellspacing="1">.*?</table></div></div>', html);
    return findData;

table = extractTable(html);
print table, "\n";

def extractDate(stringContent):
    findDate = re.findall('<trclass="stathead"><tdcolspan="7">(.*)</td></tr><trclass="colhead">', stringContent);
    if (findDate):
        return findDate;
    else:
        return 'nothing';

def extractHome(stringContent):
    findHome = re.findall('<tdalign="right"><ahref=.*>(.*)</a></td><tdalign="center">', stringContent);
    print findHome;
    return findHome;

def extractScore(stringContent):
    findScore = re.findall('<tdalign="center"><ahref=.*>(.-.)</a></td><tdalign="left">', stringContent);
    return findScore;

def extractAway(stringContent):
    findAway = re.findall('<tdalign="left"><ahref=.*>(.*?)</a></td>', stringContent);
    return findAway;

for a in range(len(table)):
    print table[a], "1\n";
    Date = extractDate(table[a]);
    print "Date: ", Date, "1\n";
    Home = extractHome(table[a]);
    #print "Home: ", Home;
    print "1\n";
    Score = extractScore(table[a]);
    print "Score: ", Score;
    print "1\n";
    Away = extractAway(table[a]);
    print "Away: ", Away;
    print "1\n";



# pattern='<tableclass="tablehead"cellpadding="3"cellspacing="1">.*</table></div></div>';
 
# for match in re.finditer(pattern,html):
#     s=match.start()
#     e=match.end()
#     print "Found %s at %d,%d" % (text[s:e],s,e)




# findDate = re.findall('<tableclass="tablehead"cellpadding="3"cellspacing="1">.*?</table></div></div>', html);
# if (findDate):
#     #print "start date: ", findDate;
#     #fDate = findDate.group();
#     print "start date: ", findDate;
findHome = re.findall('<td align="right"><a href=.*>(.*)</a></td>', html1);
if (findHome):
    #print "start date: ", findHome;
    #fHome = findHome.group();
    print "11111home: ", findHome;
# findScore = re.findall('<tdalign="center"><ahref=.*>(.*)</a></td>', html);
# if (findScore):
#     #print "start date: ", findScore;
#     #fScore = findScore.group();
#     print "  ", findScore, "  ";
# findAway = re.findall('<tdalign="left"><ahref=.*>(.*)</a></td>', html);
# if (findAway):
#     #print "start date: ", findAway;
#     #fAway = findAway.group();
#     print "away: ", findAway;
# #print "home: ", findHome, "  ", findScore, "  ", "away:", findAway;