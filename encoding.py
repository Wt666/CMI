import chardet
import coding
import urllib.request

def encoding(msg):
    result = chardet.detect(msg)
    return result['encoding']
a=urllib.request.urlopen('http://yahoo.co.jp/').read()
# print(encoding('abcd'))
# print(coding.string_encoding("abcd"))
print(chardet.detect(a))