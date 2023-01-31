import pandas as pd
import datetime

df = pd.read_csv('tweet_search_result.csv')
# df = df.groupby("created_at").count()
df["created_date"] = pd.to_datetime(df["created_at"], format = '%Y-%m-%d').dt.date

df = df.groupby("created_date").count()

# print(df.head())
df.to_csv('tweet_agg_result.csv',index = True)
