import time
import requests
import json

url = "https://cloudsms-new.jegotrip.com.cn:1815/uips"
local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
data ={
    "uip_head": {
        "METHOD": "DR_QUERY",
        "SERIAL": 1,
        "TIME": local_time,
        "CHANNEL": "CMIPB", # Please use your tenant name, which is assigned by CloudSMS
        "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw=="
    },
    "uip_body": {
        "SMS_UID":["5E7858F619664X28AHFA163E9DC506"]
    },
    "uip_version": 2
}

data = json.dumps(data)
print("Json: ", data)
rsp = requests.post(url, data, verify=False).content.decode('utf-8')
print(rsp)
rsp_new = json.loads(rsp)
print(rsp_new['uip_body'])
# print(rsp_new)