import pandas as pd

df = pd.read_csv('test.csv')
print(df.head())
'''
   log_id        date   name  quantity
0  '0001'  2022/05/01  'aaa'       100
1  '0002'  2022/05/05  'bbb'       200
2  '0003'  2022/06/01  'aaa'       150
'''

df = df['name']
print(df.head())
'''
0    'aaa'
1    'bbb'
2    'aaa'
'''
df = df[df["quantity"] >= 200]
print(df.head())
'''
   log_id        date   name  quantity
1  '0002'  2022/05/05  'bbb'       200
'''
df = df.groupby("name").sum('quantity')
print(df.head())
'''
       quantity
name           
'aaa'       250
'bbb'       200
'''

df = df.groupby("name").count()
print(df.head())
'''
       log_id  date  quantity
name                         
'aaa'       2     2         2
'bbb'       1     1         1
'''
