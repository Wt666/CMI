import re
from lxml import html
import requests
url = "http://www.europarl.europa.eu/news/en/press-room/page/"
list_of_links = []
for page in range(10):
    r = requests.get(url + str(page))
    source = r.content
    page_source = html.fromstring(source)
    list_of_links.extend(page_source.xpath('//a[@title="Read more"]/@href'))
print(list_of_links)

rule="^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
rule1="https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall(rule1, string)
    return url


string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com 我自己的是546as.cn'
print("Urls: ", Find(string))


url_pattern = re.compile("^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")
url_pattern1 = re.compile("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$") # Http
def is_valid_url(url):
    if url_pattern1.match(url):
        return True
    else:
        return False
for i in list_of_links:
    print(is_valid_url(i))

print(is_valid_url('www.runoob.com'))



# pattern = r"\u3000hello\u0020world"
# string = "　hello world"
#
# match_obj = re.search(pattern, string)
#
# if match_obj:
#     print("匹配成功！")
# else:
#     print("匹配失败！")
#
#
# from urllib.parse import urlparse
#
# def is_valid_url1(url):
#     parsed = urlparse(url)
#     if bool(parsed.scheme) and bool(parsed.netloc):
#         return True
#     else:
#         return False
# print(is_valid_url1('asdadwa.com'))