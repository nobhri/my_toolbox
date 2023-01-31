# coding: utf-8
'''
# before use This script...

## Prepare archive file
- Get archive from Twitter.
- We use tweets.js from the archive
- Put tweets.js in this directory.
- Delete 'window.YTD.tweets.part0 = ' from tweets.js

## write your key and token in your machine's environment variable like below
export CONSUMER_KEY="xxxxxxxxxxxxxxx"
export CONSUMER_SECRET="xxxxxxxxxxxxxxx"
export ACCESS_TOKEN="xxxxxxxxxxxxxxx"
export ACCESS_TOKEN_SECRET="xxxxxxxxxxxxxxx"
'''

import os
import datetime
from dateutil import tz
import json
import tweepy



print('set maximum YYYYMMDD')
target_ymd  = input()
target_ymd = datetime.datetime(
                int(target_ymd[:4]), # YYYY
                int(target_ymd[4:6]), # MM
                int(target_ymd[6:]), # DD
                tzinfo = tz.gettz('UTC'))# Timezone


print(f'Tweets until {str(target_ymd)} is going to delete.')

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

with open('tweets.js', encoding='utf-8', mode='r') as f:
    tweets = json.load(f) 
    counter = 0
    
    for tweet_i in tweets:
        tweet_datetime = tweet_i['tweet']['created_at']
        tweet_datetime = datetime.datetime.strptime(tweet_datetime, "%a %b %d %H:%M:%S %z %Y")
        tweet_text = tweet_i['tweet']['full_text']
        tweet_id = tweet_i['tweet']['id']
        if tweet_datetime <= target_ymd:
            print(tweet_datetime)
            print(tweet_text)
            print(tweet_id)
            try:
                api.destroy_status(tweet_id)
                counter += 1
            except Exception as e:
                print(e.args)

print(f'{counter} tweets has deleted')

