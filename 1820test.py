import requests
import time
import json
import urllib3

urllib3.disable_warnings()
import random

# str = ""
# for i in range(6):
#     ch = chr(random.randrange(ord('0'), ord('9') + 1))
#     str += ch
# print(str)
# print(f"【无忧行】验证码为:{str}。您当前正在通过话费支付方式办理套餐，资费标准123元，如非本人操作，请勿泄露验证码信息，任何索取验证码行为均可能涉及诈骗。")
local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

url = "https://cloudsms.jegotrip.com:1820/uips"
# numbers=["8615716703639","8618420665911","8613925055057","8613810033044","8613911472159","8613510603952","8614714311440","8618599930413","8613007493331","8613341319791"]
# numbers = ["2348098535242", "2348161553670", "2349083517299", "2348138813383", "2347033131675", "2348025619995"]
numbers = ["66621535945"]
# numbers = ["8618928488431","8613145876355","8618938939925","8613133838616","8618675563526"] #"8618938939925","8613133838616","8618675563526"
for number in numbers:
    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
        data = {
            "uip_head": {
                "METHOD": "SMS_SEND_REQUEST",
                "SERIAL": 1,
                "TIME": local_time,
                "CHANNEL": "AID_HTTPT16740308875DAPO",
                "AUTH_KEY": "M9l+6IHUz3kwiXt5qzSwY#3cSbNSBA88H1O7J9iayPX1Q40x71wn#MKQUE6HeWbspaZXjYc2qSsKtNwx7wiHmw=="
            },
            "uip_body": {
                "SMS_CONTENT": "Final call!! CC DOUBLE O Final Sale 70% off starts today (8 - 12 Jan 2024) at www.ccdoubleo.com and CC DOUBLE O stores",
                "DESTINATION_ADDR": [
                    number
                ],
                "ORIGINAL_ADDR": "CCDOUBLEO", #1069085211024009003  106575864009
                # "SIGNATURE": "无忧行",
                # "SIGNATURE_TYPE":"HEAD_BOLDFACE_SQUARE",
                # "ORDER_NUMBER": "GOI_1685434186EJUYR",
            },
            "uip_version": 2
        }
    data = json.dumps(data)
    print("\nreq:{}".format(data))
    rsp = requests.post(url, data, verify=False)
    print("\nrsq:{}".format(rsp.text))
