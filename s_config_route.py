# 注册SMPP租户及绑定路由

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
        "OPER_TYPE": "ADD",                  # ADD/INQ/UPDATE/DEL等操作类型
        "PTL_NAME": "mitry.feishu.cn/sh",  # 物理通道名或租户具体通道名
        "MODULE_NAME": "smpp",  # SMS协议模块名
        "TENANT_NAME": "CMIPB",  # 租户名
        "REGISTE_TYPE": "SERVER",  # 注册类型
        "SEND_THRESHOLD": "20",  # 若无特别需求，默认为20
        "RECV_THRESHOLD": "20",  # 若无特别需求，默认为20
        # SMPP模块
        "SYSTEM_ID": "mitry.feishu.cn/sh",  # smpp的systemID
        "PASSWORD": "XP9yqD8w",  # systemID的密码
        "SERVER_TYPE": "SMPP_SERVER",  # 配置SMPP client端取值:SMPP_CLIENT
        "IP": "8.8.8.8",  # SMPP_CLIENT:远端IP
        "PORT": 2775,  # SMPP_CLIENT:远端IP
        "MAX_LINK": 1,  # 最多允许链接数量，默认为：1,
        "ROUTE_ID": "Marketing_82",  # 业务通道映射
        # "REPORT_URL": "",  # 设置租户的DR回调地址
        "MNC_OA_LIST": [
            {
                "MCC": "1",
                "OA": "106575864009"
            },
            {
                "MCC": "2",
                "OA": "1069085211024009003"
            },
            {
                "MCC": "5",
                "OA": "CloudSMS"
            }
        ],
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
