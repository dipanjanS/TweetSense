import sys
import json
import types

def parse_sentimentfile(sf) :
    fp = open(sf)
    lines = fp.readlines()
    dictionary = dict()
    
    for line in lines :
        line = line.strip()
        key, val = line.split("\t")
        dictionary[key.strip()] = val.strip()
    fp.close()
    return dictionary

def calculate_happiest_state(sent_file, tweet_file) :
    dictionary = parse_sentimentfile(sent_file)

    fp = open(tweet_file)
    lines = fp.readlines()
    happiest = {}
    
    for line in lines :
        line = line.strip()
        jsondata = json.loads(line)

        if jsondata.has_key('place') and (type(jsondata['place']) != type(None)) and jsondata['place']['country_code'] == "US" and jsondata.has_key('text') :
            state = jsondata['place']['full_name'].encode("utf-8")[-2:]
            tweetwordlist = jsondata['text'].encode("utf-8").split()
            score = 0.0

            for tweetword in tweetwordlist :
                tweetword = tweetword.strip()
                tweetword = str.lower(tweetword)

                if tweetword in dictionary.keys() :
                    score = score + float(dictionary[tweetword])
                else :
                    score = score + 0.0
            
            if state not in happiest.keys() :
                happiest[state] = score
            else :
                if happiest[state] < score :
                    happiest[state] = score
                
    fp.close()
    
    print max(happiest, key = happiest.get)

    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

    calculate_happiest_state(sent_file, tweet_file)    


if __name__ == '__main__':
    main()
