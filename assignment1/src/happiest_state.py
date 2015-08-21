import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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
                if len(word)>1:
                    try:
                        s = score_dict[word]
                        sum_score += s
                    except:
                        pass     
        except:
            pass
        scores.append(sum_score)
    return scores

def get_scores_per_state(tweets,scores):
    scores_per_state = {}
    tweets_per_state = {}
    for i in range(len(tweets)):
        t = tweets[i]
        s = scores[i]
        try:
            if(t["place"]["country_code"]=="US"):
                state_str = t["place"]["full_name"].split(", ")
                state = state_str[1]
                if states.has_key(state):
                    try:
                        scores_per_state[state] += float(s)
                        tweets_per_state[state] += 1.0
                    except:
                        scores_per_state[state] = float(s)
                        tweets_per_state[state] = 1.0                 
        except:
            pass
    for s,v in states.items():
        if scores_per_state.has_key(s):
            scores_per_state[s] /= tweets_per_state[s]
    
    return scores_per_state
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweets = parse_tweet_file(tweet_file)
    score_dict = make_dictionary(sent_file)  
    scores = get_scores_for_tweets(tweets,score_dict)
    scores_per_state = get_scores_per_state(tweets,scores)
    s_scores = sorted(scores_per_state.items(), key=lambda x: x[1], reverse = True)
    print s_scores[0][0]

if __name__ == '__main__':
    main()
