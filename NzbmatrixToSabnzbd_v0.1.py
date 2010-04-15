import urllib2,urllib,re

##################################################
#In this section all you information is declared #
##################################################

#Url is you mzbmatrix rss feed for your bookmarks
url = 'URL'

#matrixuser is your nzbmatrix username
matrixuser = 'user'

#User is your Sabnzbd username
user = 'user'

#pass is your Sabnzbd password
password = 'password'

#Host and Port is sabnzbd (default is localhost and 8080)
host = 'localhost'
port = '8080'
api = 'apikey'

req = urllib2.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
response = urllib2.urlopen(req)
link=response.read()
response.close()
match=re.compile('<title>(.+?)</title>\n\t\t\t<guid>(.+?)</guid>\n\t\t\t<link>http://nzbmatrix.com/api-nzb-download.php\?id=(.+?)&amp;username=.+?</link>\\n\\t\\t\\t<description><!\[CDATA\[<b>Name:</b>.+?<br /><b>Category:</b> (.+?): .+?<br /><b>Hits:</b>').findall(link)


i=len(match)
s=0
while (i>s):
# adress = match[s][1]
 try:
  f = open("log.txt", "r")
  try:
   lines = f.read()
  finally:
   f.close()
 except IOError:
  pass

 idd = match[s][2]
 adress = 'http://nzbmatrix.com/api-nzb-download.php?id=' + idd 
 cat = match[s][3]
 test = re.search(idd, lines) 
 if (test != None):
  print match[s][0]
  print 'is allrdy downloaded - empty your bookmarks'
 else :
  url='http://' + host + ':' + port + '/sabnzbd/api?mode=addurl&ma_username=' + user + '&ma_password=' + password + '&name=' + adress + '&cat=' + cat+ '&apikey=' + api
  print url
  req = urllib2.Request(url)
  req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response = urllib2.urlopen(req)
  link=response.read()
  try:
   logfile = open("log.txt", "a")
   try:
    logfile.write(idd + '\n')
   finally:
    logfile.close()
  except IOError:
   pass
  print match[s][0] + ' is add to Sabnzbds que in the ' + cat + ' category'
 s=s+1 
