# 3. STG环境Portal展示数据包

# windows 系统下 tornado 使用 SelectorEventLoop
import platform

if platform.system() == "Windows":
    import asyncio

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tornado.web
import tornado.ioloop
import requests
import time
import json

url_base = {
    "my_test_company": "http://172.22.223.96:1819/uip",
}
url = url_base["my_test_company"]


def save_file(file_name, data, rsp):
    with open(file_name, "a") as f:
        f.write("\nRequest Data: \n")
        f.write(data)
        f.write("\nRespond Data: \n")
        f.write(rsp)


hkt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

data = {
    "uip_head": {
        "METHOD": "SMS_ADD_ATOM_PTL_NAME",
        "SERIAL": 1,
        "TIME": hkt,
        "CHANNEL": "CMIPB",  # 固定CHANNEL
        "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw=="  # 固定AUTH_KEY
    },
    "uip_version": 2,
    "uip_body": {
        "TENANT_NAME": "CPB98CMI01",  # 租户名
        "PTL_NAME": "CPB98CMI01",  # 下游原子通道名
        "NOTE_NAME": "ZMCS-14277",  # 下游原子通道别名（供应商简写-UID)
        "MODULE_NAME": "smpp",  # 注册模块名
        # VerifyCode,Notification,Marketing
        "SMS_TYPE": "VerifyCode,Notification,Marketing",
        "TREATY_TYPE": "smpp",
        "VERSION": "2021-04-23"
    },
}


data = json.dumps(data)
print("请求数据包:\n{}".format(data))
rsp = requests.post(
    url, data, verify=False).content.decode('utf-8')
print("响应数据包:\n{}".format(rsp))


class IndexHandler(tornado.web.RequestHandler):
    def post(self):
        jsonbyte = self.request.body
        jsonstr = jsonbyte.decode('utf-8')
        print(jsonstr)


if __name__ == "__main__":
    app = tornado.web.Application(
        [(r'/', IndexHandler)], static_path='static', debug=True, autoreload=False)
    app.listen(59999)
    tornado.ioloop.IOLoop.current().start()
