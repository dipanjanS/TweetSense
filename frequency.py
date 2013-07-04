import sys
import json

def process_tweetfile(filename):
    tweets=[]
    wordfreq = {}
    total = 0
    
    fp = open(filename)
    lines = fp.readlines()
    get = wordfreq.get
    for line in lines:
        line = line.strip()
        jsondata = json.loads(line)
        
        if 'text' in jsondata.keys():
            tweet = jsondata['text']
            tweet = tweet.split()
            
            for word in tweet:
                    wordfreq[word] = get(word, 0) + 1
                    total = total + 1.0
    
    for key in wordfreq:
        print key.encode("utf-8")+" "+str(float(wordfreq[key]/total))
         
    fp.close()

    
def main():
    
    tweet_file = sys.argv[1]
    process_tweetfile(tweet_file)

if __name__ == '__main__':
    main()
