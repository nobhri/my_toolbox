# coding: utf-8

import os
import tweepy



consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']


auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)
text = "I made plot for something."
plt_file_name = 'tweet_search_plot.png'

api.update_status_with_media(status = text , filename = plt_file_name)
