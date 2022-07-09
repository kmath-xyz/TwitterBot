#modules
import tweepy
from Keys import *

#main
client = tweepy.Client(consumer_key=api_key ,consumer_secret= api_sec,access_token=acc_token,access_token_secret=acc_sec)
auth = tweepy.OAuthHandler(api_key, api_sec)
auth.set_access_token(acc_token, acc_sec)

api = tweepy.API(auth)

tweet=input("Your Tweet:")

client.create_tweet(text=tweet)


