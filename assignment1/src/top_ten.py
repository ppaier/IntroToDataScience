import sys
import json

def parse_tweet_file(fp):
    tweets = []
    for line in fp:
        obj = json.loads(line)
        tweets.append(obj)
    return tweets

def get_hash_frequencies(tweets):
    frequencies = {}
    for t in tweets:
        try:
            hashtags = t["entities"]["hashtags"]
            for ht in hashtags:      
                try:
                    frequencies[ht["text"]] += 1
                except:
                    frequencies[ht["text"]] = 1
        except:
            pass
    return frequencies


def main():
    tweet_file = open(sys.argv[1])
    tweets = parse_tweet_file(tweet_file) 
    frequencies = get_hash_frequencies(tweets)
    s_frequ = sorted(frequencies.items(), key=lambda x: x[1], reverse = True)
    count = 10
    for k,v in s_frequ:
        if count == 0:
            break
        try:
            print '%s %d' %(k,v)
        except:
            print '%s %d' %(k.encode('utf-8'),v)
        count -= 1

if __name__ == '__main__':
    main()
