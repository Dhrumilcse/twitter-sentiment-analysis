import tweepy
from textblob import TextBlob

#Create your app from apps.twitter.com and fill your keys
consumer_key = '3KFL*************'
consumer_secret = 'yltO********************'
access_token = '3014895**************'
access_token_secret = 'w7rZ********************'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Narendra Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('\n')