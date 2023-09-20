import requests
import json
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
# url = 'https://vid1038.trvdp.com/media/80364fb35c53f12e7231a8623006b584c2e66828/hls/80364fb35c53f12e7231a8623006b584c2e66828_240_00004.ts'
# data = requests.get(url).text
#
# new_data = json.loads(data)
# print(new_data)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
response=requests.get("https://www.am730.com.hk/",headers=headers)
# print(response.text)
soup = BeautifulSoup (response.content, "html.parser")
#Get all topicitems
Items = soup.find_all ("div", class_= "newsitem")
newsitems = soup.find_all('div', class_='newsitem')
data = []
for item in newsitems:
    href = item.find('a').get('href')
    data_src = item.find('img').get('data-src')
    data.append([href, data_src])

# 将数据输出到Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['href', 'data-src'])
for row in data:
    ws.append(row)
wb.save('output.xlsx')
# Create an empty DataFrame
# df = pd.DataFrame(columns = ["href", "data-src"])
#
# # Go through all items
# href=[]
# data_src=[]
# for item in Items:
#     href.append(item ["href"])
#     data_src.append(item.find ("img") ["data-src"])
#     # Href = item["href"]
#     # data_src = item.find("img")["data-src"]
# # Df=pd.DataFrame({"href": href, "data-src": data_src})
# # print(Df)
#
# print(href)
# print(data_src)
# Df = df.append(pd.DataFrame({"href": href, "data-src": data_src}), ignore_index = True)

#Write to Excel file
# Df.to_excel ("url1.xlsx", index = False)