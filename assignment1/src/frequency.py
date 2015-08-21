import sys
import json

def parse_tweet_file(fp):
    tweets = []
    for line in fp:
        obj = json.loads(line)
        tweets.append(obj)
    return tweets

def get_term_frequencies(tweets):
    frequencies = {}
    overall_terms = 0
    for t in tweets:
        try:
            text = t["text"].replace('\n',' ')
            text = text.replace('.',' ')
            text = text.replace(',',' ')
            text = text.replace(';',' ')
            text = text.replace('\t',' ')
            text = text.split(' ')
            for word in text:
                if len(word)>1:                
                    overall_terms += 1
                    try:
                        frequencies[word] += 1
                    except:
                        frequencies[word] = 1
        except:
            pass
    for k,v in frequencies.items():
        frequencies[k] = float(frequencies[k])/overall_terms   
    return frequencies


def main():
    tweet_file = open(sys.argv[1])
    tweets = parse_tweet_file(tweet_file) 
    frequencies = get_term_frequencies(tweets)
    for k, v in frequencies.items():
        try:
            print '%s %f' %(k,v)
        except:
            pass #print '%s %f' %(k.encode('utf-8'),v)

if __name__ == '__main__':
    main()
