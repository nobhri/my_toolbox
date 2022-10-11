# coding: utf-8

import os
import datetime
from dateutil import tz
import tweepy


print('set maximum YYYYMMDD')
target_ymd  = input()
target_ymd = datetime.datetime(
                int(target_ymd[:4]), # YYYY
                int(target_ymd[4:6]), # MM
                int(target_ymd[6:]), # DD
                tzinfo = tz.gettz('UTC'))# Timezone


print(f'Tweets until {str(target_ymd)} is going to dalete.')

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


counter = 0
for tweet_i in tweepy.Cursor(api.user_timeline).items():
    if tweet_i.created_at <= target_ymd:
        print(tweet_i.created_at)
        print(tweet_i.text)
        api.destroy_status(tweet_i.id)
        counter += 1

print(f'{counter} tweets has deleted')

