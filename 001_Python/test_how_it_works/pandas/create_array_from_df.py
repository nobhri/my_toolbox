import pandas as pd

df = pd.read_csv('test.csv')
# print(df.head())
new_array = df.to_numpy()
print(new_array)