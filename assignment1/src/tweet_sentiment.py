import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def make_dictionary(fp):
    scores = {}
    for line in fp:
        term , score = line.split("\t")
        scores[term] = int(score)
    #print scores.items()
    return scores

def parse_tweet_file(fp):
    tweets = []
    for line in fp:
        obj = json.loads(line)
        tweets.append(obj)
    return tweets

def get_scores_for_tweets(tweets,score_dict):
    for t in tweets:
        try:
            text = t["text"].replace('\n',' ')
            text = text.replace('.',' ')
            text = text.replace(',',' ')
            text = text.replace(';',' ')
            text = text.replace('\t',' ')
            text = text.split(' ')
            
            sum_score = 0
            for word in text:
                if len(word)>1:
                    try:
                        s = score_dict[word]
                        sum_score += s
                    except:
                        sum_score += 0
            print sum_score        
        except:
            print 0

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweets = parse_tweet_file(tweet_file)
    score_dict = make_dictionary(sent_file)  
    get_scores_for_tweets(tweets,score_dict)


if __name__ == '__main__':
    main()
