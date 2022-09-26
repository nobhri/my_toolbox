import pandas as pd

data_list = [
    ['hot guitar', 'guitar', 2000],
    ['good to blow', 'sax', 5000],
    ['funk machine', 'bass guitar', 3000],
    ]

column_list = [
    'name', 'category', 'price' 
    ]

df = pd.DataFrame(data = data_list, columns = column_list)
print(df.head())