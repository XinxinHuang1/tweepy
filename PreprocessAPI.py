import tweepy;
import json;
import pandas as pd;

consumer_key = 'consumer'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#1: write @Google's most recent 100 tweets to JSON file
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

relself_tweets = api.user_timeline(screen_name = 'Google',count = 100)
with open('@Google_tweets.json', 'w') as json_file:
    for t in relself_tweets:
        json.dump(t, json_file)
        json_file.write('\n')
print('Message: @realself tweets saved to @Google_tweets.JSON', '\n')

#2: count unique hashtags for tweets with #Seattle
API = tweepy.API(auth)
tweets = tweepy.Cursor(API.search, q = '#Seattle'.lower()).items(100)
df1 = []
for t in tweets:
    ht = (t.entities.get('hashtags'))
    for h in ht:
        df = list(pd.DataFrame(h).text.unique())
        df1.append(df)

for hashtag in set(map(tuple, df1)):
    print ('{} frequency -> {}'.format(hashtag, df1.count(list(hashtag))))
