import sys
import json
import heapq
from operator import itemgetter

def process_tweetfile(filename):
    tweets=[]
    hashtagfreq = {}
    total = 0
    
    fp = open(filename)
    lines = fp.readlines()
    get = hashtagfreq.get
    
    for line in lines:
        line = line.strip()
        jsondata = json.loads(line)

        if 'entities' in jsondata.keys():
            if jsondata['entities']['hashtags'] != []:
                for i in range(len(jsondata['entities']['hashtags'])):
                    hashtag = (jsondata['entities']['hashtags'][i]['text']).encode("utf-8")
                    hashtagfreq[hashtag] = get(hashtag, 0.0) + 1.0

    top_ten = heapq.nlargest(10, hashtagfreq.items(), key=itemgetter(1))
    for i in range(len(top_ten)):
        print top_ten[i][0]+" "+str(top_ten[i][1])
        
    fp.close()

    
def main():

    tweet_file = sys.argv[1]
    process_tweetfile(tweet_file)

if __name__ == '__main__':
    main()
