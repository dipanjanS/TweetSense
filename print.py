import urllib
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

page = 1
while page <= 10:
    response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page="+str(page))
    data = json.load(response)

    print "\n-------------------------------- Page "+str(page)+" Tweets ---------------------------------"
    i=0
    while i < len(data['results']):
        line = str(data['results'][i]['text'])
        print line.encode("utf-8")
        i = i + 1
    print "-------------------------------------------------------------------------------\n"
    page = page + 1
    


