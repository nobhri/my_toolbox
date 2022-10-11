# Pythonで特定の日付以前の過去のTweetを消去する

## やること  
- Pythonで特定の日付以前の過去のTweetを消去する。

## 背景
- qiitaでも書くか～って思ったときに、Twitterアカウントをプロフィールに乗せたい気がする。
- あまりにも昔のTweetが残っていると恥ずかしい。
- でも最近のTweetは残しておきたい。

## 想定読者
- 自力でツイ消しプログラムを書きたい人
- 全件消すのではなく、特定の日付以前のTweetのみを消去したい人
- Pythonの基本的な文法がわかる人
- Linuxの環境変数設定がわかる人
- TwitterAPIのトークンなどの発行方法がわかる人
- Twitterからアーカイブを取得する方法がわかる人

## 概要
- コマンドラインから入力した年月日以前のツイートを消すスクリプト。
- TwitterにアクセスするためのPythonライブラリはtweepyを使用。多分なんでもいいと思う。
- TimezoneはUTCにしてある。

## 作業手順
- 実行する前にTwitterから取得したアーカイブファイルtweets.jsをpythonスクリプトと同じディレクトリに配置する。
- tweets.jsはじめの`window.YTD.tweets.part0 = `という部分は消しておく。
- 事前にマシンの環境変数にkeyやtokenを書いておく __Pythonファイル内にベタ書きしてgitに上げるとえらいことになるから注意__
- コマンドラインでスクリプトを実行する。
- 消したい期間の最終日付を`YYYYmmDD`形式で入力する。

## ソースコード
```python
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
```


## 感想
- 最初は`api.user_timeline`から順番にツイートを呼び出せると思ったが、件数制限で引っかかって撃沈した。悲しい。
- アーカイブのJSONの中身を確認するのが大変だった。階層構造のどこに何が入っているかとか、日付のフォーマットとか。

## まとめ  
これで皆さんも、垢バレに備えて程ほどにツイ消しできますね。  
よいTwitterライフを!!  

## 参考記事
[Twitter API と Python でツイートを一括削除](https://mytech-blog.com/twitter-api-python/)