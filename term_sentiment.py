import sys
import json


reload(sys)
sys.setdefaultencoding("utf-8")


def process_tweetfile(filename):
    tweets=[]
    fp = open(filename)
    lines = fp.readlines()
    for line in lines:
        line = line.strip()
        jsondata = json.loads(line)
        if 'text' in jsondata.keys():
            tweet = jsondata['text'].strip().encode("utf-8")
            tweets.append(tweet)
    fp.close()
    return tweets
    

def create_dict(filename):
    database = {}
    fp = open(filename)
    lines = fp.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        database[key] = value
    fp.close()
    return database
    
    
def calc_sentiment(sentiment_file,tweet_file):

    tweets = process_tweetfile(tweet_file)
    database = create_dict(sentiment_file)
    scores = []
    sentdict = {}
    for tweet in tweets:

        score = 0.0
        words = tweet.split()

        for word in words:
            word = str.lower(word)
            
            if word in database.keys():
                value = float(database[word])
                score = score + value
                    
        
        for word in words:
            

            if word not in sentdict.keys():
                sentdict[word] = score
            else:
                sentdict[word] = sentdict[word] + score

    for key in sentdict:
        print key.encode("utf-8")+" "+str(sentdict[key])
    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    #process_tweetfile(tweet_file)
    calc_sentiment(sent_file,tweet_file)

if __name__ == '__main__':
    main()
