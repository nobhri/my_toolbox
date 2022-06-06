# 20220606_03_plot_data.py
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('tweet_agg_result.csv')
# df.to_csv('tweet_agg_result.csv',index = True)

# print(df.head())

plt.figure()# initialize plt
df.plot(x = 'created_date', y = 'text', kind = 'bar', rot = 45)
# plt.show()
plt.savefig('tweet_search_plot.png')# save as .png image file