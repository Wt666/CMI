# 注册API租户

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
        "METHOD": "SMS_REGISTER_REQUEST",
        "SERIAL": 1,
        "TIME": hkt,
        "CHANNEL": "CMIPB",  # 固定CHANNEL
        "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw=="  # 固定AUTH_KEY
    },
    "uip_version": 2,
    "uip_body": {
        "OPER_TYPE": "ADD",  # UPDATE  ,ADD
        "PTL_NAME": "PTIMS",
        "MODULE_NAME": "smsgate",
        "TENANT_NAME": "PTIMS",
        "REGISTE_TYPE": "CLIENT",
        "SEND_THRESHOLD": "5",  # 条数
        "RECV_THRESHOLD": "5",  # 条数
        "VERSION": "2021-04-23",
        "REPORT_URL": "",  # 设置租户的DR回调地址
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
