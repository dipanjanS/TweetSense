import sys
import json

def find_top_ten(tweet_file) :
    fp = open(tweet_file)
    lines = fp.readlines()

    hashtaglist = {}
            
    for line in lines :
        line = line.strip()
        jsondata = json.loads(line)
        
        if jsondata.has_key('entities') and jsondata['entities']['hashtags'] != [] :
            for i in range(len(jsondata['entities']['hashtags'])):
                hashtag = jsondata['entities']['hashtags'][i]['text'].encode("utf-8")
            
                if hashtag not in hashtaglist.keys() :
                    hashtaglist[hashtag] = 1.0
                else :
                    hashtaglist[hashtag] = hashtaglist[hashtag] + 1.0

    fp.close()

    for key in (sorted(hashtaglist, key=hashtaglist.get,reverse=True)[:10]) :
        print key+" "+str(hashtaglist[key])

    
def main():
    tweet_file = sys.argv[1]
    find_top_ten(tweet_file)
                           
if __name__ == '__main__':
    main()
