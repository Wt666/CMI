import tornado.web
import tornado.ioloop
import requests
import time
import json

local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(local_time)
url = "https://stg-cloudsms.jegotrip.com.cn:61815/uips"
data = {
    "uip_head":{
        "METHOD":"SMS_CONVERSION",
        "SERIAL":1,
        "TIME":"UTC+8 2022-04-21 11:01:07",
        "CHANNEL":"CMIPB",
       "AUTH_KEY":"cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwJUdZGJSHkr+YhD+XbeKgfowmFEAdh0qoXSpGb+A7Y7Yg=="
    },
    "uip_body":{
        "SMS_UID":"5DD2077B2787DXA1FHFA163E017E52",
        "RECEIVED":"TRUE",
        "RECEIVED_TYPE":"HTTP_RECEIVED",
        "VERSION":"2022-02-09"
    },
    "uip_version":2
}
data = json.dumps(data)
print("Json: ", data)
rsp = requests.post(url, data, verify=False).content.decode('utf-8')
print(rsp)
rsp_new = json.loads(rsp)
print(rsp_new['uip_head']['RESULT_CODE'])
# code = rsp_new["RESULT_CODE"]
# print(code)

# class IndexHandler(tornado.web.RequestHandler):
#     def post(self):
#         jsonbyte = self.request.body
#         jsonstr = jsonbyte.decode('utf-8')
#     print(jsonstr)
#
# rsp = requests.post(url, data, verify=False).content.decode('utf-8')
# print("rsp: ", rsp)
# if __name__ == "__main__":
#     app = tornado.web.Application(
#         [(r'/', IndexHandler)], static_path='static', debug=True, autoreload=False)
#     app.listen(59999)
#     tornado.ioloop.IOLoop.current().start()
