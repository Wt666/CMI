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
    # "my_test_company": "https://172.22.223.192:1815/dave/io",  # STG的公司内网访问地址
    "my_prod_company": "https://172.22.223.96:1815/dave/io",  # prod的公司内网访问地址
}
url = url_base["my_prod_company"]


def save_file(file_name, data, rsp):
    with open(file_name, "a") as f:
        f.write("\nRequest Data: \n")
        f.write(data)
        f.write("\nRespond Data: \n")
        f.write(rsp)


hkt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 测试接收电话号码
phone = {
    "62": [8989583828],
}

# 短信模板
template = {
    "CloudSMS": "Your verification code is 123456",
    # "CloudSMS": "[SHLCWH] Your code is 208852.",
}

try:
    # 测试为每个模板向不同账号发送,休眠5分钟后,切换模板发送。
    # 每个模板的标题

    for tem in template.keys():
        # 每个国家码
        for cc in phone.keys():
            # 对应国家码下的每个电话号码
            for number in phone[cc]:
                # 获取当前发送时间
                local_time = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime())

                data = {
                    "METHOD": "SMS_SEND_REQUEST",
                    "TYPE": "REQUEST",
                    "SERIAL": 1,
                    "TIME": local_time,
                    "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw==",
                    # STG测试号
                    "ROUTE_ID": "ZMCS_Notification",
                    "PRIORITY": 0,
                    # "SIGNATURE_TYPE": 1,
                    "VERSION": "2020-07-12",
                    "SMS_CONTENT": template[tem],
                    "ORIGINAL_ADDR": tem,
                    # "SIGNATURE": tem,
                    "MULTI_MSISDN_LIST": [{"DEST_MSISDN": str(number),
                                           "COUNTRY_CODE": int(cc)}],
                }

                data = json.dumps(data)
                print("请求数据包:\n{}".format(data))
                rsp = requests.post(
                    url, data, verify=False).content.decode('utf-8')
                print("响应数据包:\n{}".format(rsp))
                # 保存发送记录
                rsp_new = json.loads(rsp)
                code = rsp_new["RESULT_CODE"]
                # 发送成功的记录（保存为两个文件）
                if code == 1:
                    save_file(file_name="STG_Success.txt",
                              data=data, rsp=rsp)
                else:
                    save_file(file_name="STG_Fail.txt",
                              data=data, rsp=rsp)
                time.sleep(5)
        print(">>>>>>>>>>等待发送下一个模板<<<<<<<<<<")
        time.sleep(240)

except Exception as e:
    print("发送失败")
    print(e.args)



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

