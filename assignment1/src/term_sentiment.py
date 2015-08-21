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
    scores = []
    for t in tweets:
        sum_score = 0
        try:
            text = t["text"].replace('\n',' ')
            text = text.replace('.',' ')
            text = text.replace(',',' ')
            text = text.replace(';',' ')
            text = text.replace('\t',' ')
            text = text.split(' ')
            for word in text:
                try:
                    s = score_dict[word]
                    sum_score += s
                except:
                    pass
        except:
            sum_score = 0
        scores.append(sum_score)
    return scores

def get_new_score_dict(tweets, scores, old_dict):
    new_dict = {};
    for i in range(len(tweets)):
        t = tweets[i]
        try:
            text = t["text"].replace('\n',' ')
            text = text.replace('.',' ')
            text = text.replace(',',' ')
            text = text.replace(';',' ')
            text = text.replace('\t',' ')
            text = text.split(' ')            
            for word in text:
                if len(word)>3:
                    #print(word)
                    try:
                        new_dict[word] += scores[i] 
                    except:
                        new_dict[word] = 0
        except:
            pass
    return new_dict


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweets = parse_tweet_file(tweet_file)
    score_dict = make_dictionary(sent_file)  
    scores = get_scores_for_tweets(tweets,score_dict)
    #print scores
    new_dict = get_new_score_dict(tweets, scores, score_dict)
    for k, v in new_dict.items():
        try:
            print '%s %d' %(k,v)
        except:
            pass#print '%s %d' %(k.encode('utf-8'),v)

if __name__ == '__main__':
    main()
