import pandas as pd

df = pd.read_csv('test.csv')
print(df.head())

df.to_csv('test_output.csv', index = False)