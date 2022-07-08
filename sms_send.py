import platform
if platform.system() == "Windows":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import tornado.web
import tornado.ioloop
import requests
import time
import json
from tornado.httpserver import HTTPServer

url_base = {
    # "my_test_company": "https://172.22.223.192:1815/dave/io",  # STG的公司内网访问地址
    # "my_prod_company": "https://172.22.223.98:1815/dave/io",  # prod的公司内网访问地址  备环境
    "my_prod_company": "https://cloudsms-new.jegotrip.com.cn:1815/dave/io",  # prod的公司内网访问地址
}
url = url_base["my_prod_company"]

def post_and_resp(data):
    data = json.dumps(data)
    print("\n请求数据包:\n{}".format(data))
    rsp = requests.post(
        url, data, verify=False).content.decode('utf-8')
    print("响应数据包:\n{}".format(rsp))

    # 保存发送记录
    # rsp_new = json.loads(rsp)
    # code = rsp_new["RESULT_CODE"]
    # # 发送成功的记录（保存为两个文件）
    # if code != 1:
    #     print("发送异常:")
    #     print(f'sms_oa:{sms_oa}')
    #     print(f'cc:{dire}, phone:{phone}')
    #     save_file(file_name="STG_Fail.txt",
    #               data=data, rsp=rsp)
def sms_send():
    try:
        had_sent = 0
        # sms_wait = get_sms_wait()
        # sms_amount = len(dires) * len(templs) # 短信发送总量 == 国家方向个数 * 短信模板数(8)
        # print("此次产品测试短信总发送量应为：{}条".format(sms_amount))
        # print(f"分成{len(sms_wait)}个批次发送，每个批次发送后休眠5分钟")
        # for bulks in sms_wait.values():
        #     for bulk in bulks:
        #         local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {
            "METHOD": "SMS_SEND_REQUEST",
            "TYPE": "REQUEST",
            "SERIAL": 1,
            "TIME": local_time,
            "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw==",
            "ROUTE_ID": "IVEN_OTP_PPACK_TEST_VerifyCode",
            "MULTI_MSISDN_LIST":
                [
                    {
                        "DEST_MSISDN": "97734747",
                        "COUNTRY_CODE": 852
                    }
                ],
            "SMS_CONTENT": "您的验证码是123345，请勿向他人透露。",
            "SIGNATURE": "CloudSMS",  # 短信签名无需填写【】，方框将通过SIGNATURE_TYPE添加
            "SIGNATURE_TYPE": 1,  # 如使用SIGNATURE参数，请配合选择SIGNATURE_TYPE字段
            "ORIGINAL_ADDR": "",  # 参数值若不填或为空，短信将使用默认SENDERID
            "VERSION": "2021-01-01",
            "REPEAT": 0,
            "CUSTOMER_BODY": {}
        }
        post_and_resp(data)
    except Exception as e:
        print("发送失败")
    # had_sent += 1
    # if 0 < sms_amount - had_sent:
    #     print(f"已发送{had_sent}条短信，剩余{sms_amount - had_sent}条等待发送。")
    #     time.sleep(300)  # 号码休眠，降低运营商屏蔽号码的几率
    # else:
    #     print(f"发送完毕。已发送{had_sent}条短信")
    # except Exception as e:
    #     print("发送失败")
    #     print(e.args)
    #     print(str(e))
    #     print(repr(e))
    # print(结束)
if __name__ == "__main__":
    print("program begin.")
    sms_send()
    print("program done.")