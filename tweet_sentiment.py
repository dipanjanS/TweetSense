import sys
import json


reload(sys)
sys.setdefaultencoding("utf-8")


def process_tweetfile(filename):
    tweets=[]
    fp = open(filename)
    lines = fp.readlines()
    for line in lines:
        line = line.encode("utf-8").strip()
        jsondata = json.loads(line)
        tweets.append(json.loads(line))
    fp.close()
    return tweets

def process_tweets(filename):
    tweets = []
    tweetdata = process_tweetfile(filename)
    for i in range(len(tweetdata)):
        if 'text' in tweetdata[i].keys():
            tweet = (tweetdata[i]['text']).encode("utf-8")
            tweets.append(tweet)
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

    tweets = process_tweets(tweet_file)
    database = create_dict(sentiment_file)
    scores = []
    for tweet in tweets:
        score = 0.0
        words = tweet.split()
        for word in words:
            word = word.strip().encode("utf-8")
            word = str.lower(word)
            if word in database.keys():
                value = float(database[word])
                score = score + value
            else:
                score = score + 0
        scores.append(score)

    for score in scores:
        print score
    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    calc_sentiment(sent_file,tweet_file)

if __name__ == '__main__':
    main()
