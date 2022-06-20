import requests

file_url = 'URL'

file_name = 'filename.csv'
r = requests.get(file_url)
data = r.content

with open(file_name ,mode='wb') as f:
    f.write(data)