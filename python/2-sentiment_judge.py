# judge sentiment by twitter's api
import tweepy
from textblob import TextBlob

consumer_key = 'bDcKTZClaxCKYmjE0lX2mDEcg'
consumer_secret = 'ya4eAY0WFkZ9BhsztvMjt8VAp2pGfaQg0knFJ8msu99f4S3PLc'

access_token = '750889195997134852-v3rSe5bmQppHU5LuPdY0ZehECvr8WLC'
access_token_secret = 'oO5kV55r4FTJzvR7U3j4yg32AQOuzKxpJN1LAv7msUh5Z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
  print(tweet.text)
  analysis = TextBlob(tweet.text)
  print(analysis.sentiment)