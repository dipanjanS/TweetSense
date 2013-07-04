import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

def process_tweetfile(tweet_file,sentiment_file):
    tweets=[]
    happiest = {}
    database = create_dict(sentiment_file)

    fp = open(tweet_file)
    lines = fp.readlines()
   
    for line in lines:
        line = line.strip()
        jsondata = json.loads(line)
        
        if 'text' in jsondata.keys():

            if (jsondata['place'] != None) and (jsondata['place']['country_code'] == "US"):
                state = (jsondata['place']['full_name']).encode("utf-8")[-2:]
                    
                #print (jsondata['text']).encode("utf-8")+" "+(jsondata['place']['full_name']).encode("utf-8")

                tweet = (jsondata['text']).encode("utf-8")
                tweet = tweet.split()
                score = 0
                for word in tweet:
                    word = str.lower(word.strip())
                    
                    if word in database.keys():
                        value = float(database[word])
                        score = score + value
                    else:
                        score = score + 0
                
                if state not in happiest.keys():
                    happiest[state] = score
                else:
                    if happiest[state] < score:
                        happiest[state] = score
                
    print max(happiest.iterkeys(), key=(lambda key: happiest[key]))
    fp.close()


def create_dict(filename):
    database = {}
    fp = open(filename)
    lines = fp.readlines()
    for line in lines:
        key, value = line.strip().split("\t")
        database[key] = value
    fp.close()
    return database


def main():
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]
    process_tweetfile(tweet_file,sentiment_file)

if __name__ == '__main__':
    main()
