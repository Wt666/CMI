import json
import requests

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

response_dict=r.json()
readable_file = 'pcc_2e-master/chapter_17/data/readable_hn_data.json'
with open(readable_file,'w') as f:
    json.dump(response_dict,f,indent=4)