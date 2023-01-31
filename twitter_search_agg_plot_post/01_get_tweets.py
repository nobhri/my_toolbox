# coding: utf-8

import os
import datetime
import tweepy
import pandas as pd

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)


api = tweepy.API(auth)

target_date_end = datetime.datetime.today().strftime('%Y-%m-%d')
target_date_start = datetime.datetime.today() -datetime.timedelta(days =2)
target_date_start = target_date_start.strftime('%Y-%m-%d')
keyword_list = ['data', 'science']
query_key_word = '"' +  ' '.join(keyword_list) + '"'

# search_query = f'{query_key_word} OR @i since:{target_date_start} until:{target_date_end}'
search_query = f'{query_key_word} OR @i since:{target_date_start}'

# print(search_query)

tweet_list = []
for tweet_i in tweepy.Cursor(api.search_tweets, q=search_query, result_type='recent', count=100).items(17500):
    tweet_list.append([
    tweet_i.created_at,
    tweet_i.id,
    tweet_i.user.name,
    tweet_i.user.screen_name,
    tweet_i.text])
# print(tweet_list)

labels = ['created_at', 'tweet_id', 'user_name','user_screen_name','text']
df = pd.DataFrame(tweet_list, columns=labels)
print(df.head())
df.to_csv('tweet_search_result.csv', index = False)
