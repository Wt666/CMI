# 注册下游物理通道(注册下游路由通道 route channel)
# 上架下游路由通道

import requests
import time
import json

# url 对接环境
# 确认客户对接CloudSMS的环境（STG或PROD）
url_base = {
    "my_prod_company": "http://172.22.223.96:1819/uip",
}
url = url_base["my_prod_company"]

def save_file(file_name, data, rsp):
    with open(file_name, "a") as f:
        f.write("\nRequest Data: \n")
        f.write(data)
        f.write("\nRespond Data: \n")
        f.write(rsp)

def post_and_resp(data):
    '''data：json格式的参数'''
    data = json.dumps(data) # json化
    print("请求数据包:\n{}".format(data))
    rsp = requests.post(
        url, data, verify=False).content.decode('utf-8')
    print("响应数据包:\n{}".format(rsp))

# 注册下游物理通道(注册下游路由通道 route channel) ========
hkt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
PTL_NAME = 'WTT'
PASSWORD = "333"  # systemID的密码
IP = "10.91.2.1" # SMPP_CLIENT:远端IP (10.91.1.1 & 10.91.2.1) 2775 ITT节点选1(奇数) GNC节点选2
OA = 'CloudSMS' # 公共路由基本填写 CloudSMS，独立路由填写租户名称本身
NOTE_NAME = "aaaa-13123" # 下游原子通道别名（独立路由：供应商简写-UID； 公共路由如：Texcell OTP-14140)
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
        "OPER_TYPE": "ADD",  # ADD/INQ/UPDATE/DEL等操作类型
        "PTL_NAME": PTL_NAME,  # 物理通道名或租户具体通道名
        "MODULE_NAME": "smpp",  # SMS协议模块名
        "TENANT_NAME": PTL_NAME,  # 租户名
        "REGISTE_TYPE": "CLIENT",  # 注册类型
        "SEND_THRESHOLD": "20",  # 若无特别需求，默认为20
        "RECV_THRESHOLD": "20",  # 若无特别需求，默认为20
        "VERSION": "2021-04-23",
        # SMPP模块
        "SYSTEM_ID": PTL_NAME,  # smpp的systemID
        "PASSWORD": PASSWORD,  # systemID的密码
        "SERVER_TYPE": "SMPP_CLIENT",  # 配置SMPP client端取值:SMPP_CLIENT
        "IP": IP,  # SMPP_CLIENT:远端IP (10.91.1.1 & 10.91.2.1) 2775 ITT节点选1(奇数) GNC节点选2
        "PORT": 2775,  # SMPP_CLIENT:远端IP
        "MAX_LINK": 1,  # 最多允许链接数量（4），默认为：1,

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
                "OA": OA  # 公共路由基本填写 CloudSMS，独立路由填写租户名称本身
            }
        ],
    },
}
post_and_resp(data)


# 上架下游路由通道 ==========
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
        "TENANT_NAME": PTL_NAME,  # 租户名
        "PTL_NAME": PTL_NAME,  # 下游原子通道名
        "NOTE_NAME": NOTE_NAME,  # 下游原子通道别名（独立路由：供应商简写-UID； 公共路由如：Texcell OTP-14140)
        "MODULE_NAME": "smpp",  # 注册模块名
        # VerifyCode,Notification,Marketing
        "SMS_TYPE": "VerifyCode,Notification,Marketing",
        "TREATY_TYPE": "smpp",
        "VERSION": "2021-04-23"
    },
}
post_and_resp(data)


