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
        "CHANNEL": "DBFB", # Please use your tenant name, which is assigned by CloudSMS
        "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOesZw0t#vtkzcTEslGyVppQFaNPKinJ+aWU51PHgaxvi6uEDAShrx3mGiVrreL#3wA=="
    },
    "uip_body": {
        "SMS_UID":["5E804A57B5238X2A5HFA163E9DC506"]
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