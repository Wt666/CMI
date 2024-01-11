import requests
import time
import json
import urllib3


url_base = {
    # "my_test_company": "https://172.22.223.192:1815/dave/io",  # STG的公司内网访问地址
    # "my_prod_company": "https://172.22.223.96:1815/dave/io",  # prod的公司内网访问地址
    # "my_prod_company": "http://172.22.223.67:1814/jegom/jtp",  # 67环境
    # "my_prod_company": "http://172.22.223.147:1814/jegom/jtp",  # 集成环境
    # "my_prod_company": "https://192.168.11.68:1815/dave/io",  # prod的公司服务器内网访问地址
    "my_prod_company": "https://cloudsms.jegotrip.com:1827/sms/send/v1",  # API外部访问地址
    # "my_prod_company": "https://cloudsms-new.jegotrip.com.cn:1815/dave/io",  # API外部访问地址
    # "my_prod_company": "https://cloudsms-new.jegotrip.com.cn:1820/uips",  #
}
url = url_base["my_prod_company"]


def post_data(data):
    try:
        data = json.dumps(data)
        # print(data)
        # print("\nreq:{}".format(data))

        for _ in range(5):
            rsp = requests.post(url, data, verify=False)
            if rsp.status_code == 200:  # API请求正常
                return True, rsp
        # API请求异常
        return False, rsp
    except Exception as e:
        print(f'try except info: {e.args}')

# def post_and_resp(data):
#     try:
#         data = json.dumps(data)
#         print("\nreq:{}".format(data))
#
#         for _ in range(5):
#             rsp = requests.post(url, data, verify=False)
#             if rsp.status_code == 200:
#                 # API请求正常
#                 rsp_new = rsp.json()
#                 code = rsp_new["RESULT_CODE"]
#                 desc = rsp_new["RESULT_DESC"]
#                 if code == 1:
#                     print(f'API RESULT_DESC:{desc}, SMS_UID:{rsp_new["DETAIL_LIST"][0]["SMS_UID"]}')
#                     return True, rsp_new["DETAIL_LIST"][0]['SMS_UID']
#                 else:
#                     msg = f"API 响应正常，发送异常: RESULT_CODE: {code}, RESULT_DESC: {desc}, \nrsp:{rsp_new}"
#                     print(msg)
#                     return False, msg
#         # API请求异常
#         print(f'API 响应异常： rsp.status_code: {rsp.status_code}')
#         print(f'rsp.text: {rsp.text}')
#         return False, rsp.text
#     except Exception as e:
#         print(f'try except info: {e.args}')
#         traceback.print_exc()
#         info = sys.exc_info()
#         print(info)
#         return False, info

def send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key):
    # if original_addr in ['whatsapp', 'facebook']:
    #     signature = None
    # else:
    #     signature = original_addr
    '''
    单独发送一条短信
    :param sms_content: 短信内容
    :param original_addr: 也称OA或SenderID
    :param dest_msisdn: 目标手机号码（不含区号）
    :param country_code: 目标手机号码区号
    :param route_id: CloudSMS业务通道，由CloudSMS管理人员配置具体策略生成。
    :param auth_key: CloudSMS租户识别码，由CloudSMS管理人员配置具体策略生成。
    :return:
    '''
    try:
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {
            "METHOD": "SMS_SEND_REQUEST",
            "TYPE": "REQUEST",
            "SERIAL": 1,
            "TIME": local_time,
            "AUTH_KEY": auth_key,  # 租户的AUTH_KEY
            "ROUTE_ID": route_id,  # 业务通道Route_id
            # "PRIORITY": 0,
            # "SIGNATURE": 'INFO',
            # "SIGNATURE_TYPE": 1,
            "VERSION": "2021-01-01",
            "SMS_CONTENT": sms_content,
            "ORIGINAL_ADDR": original_addr,
            "MULTI_MSISDN_LIST": [{"DEST_MSISDN": str(dest_msisdn),
                                   "COUNTRY_CODE": country_code}],
            # "MULTI_MSISDN_LIST": '[{"DEST_MSISDN": "91652018", "COUNTRY_CODE": 62}]',

        }

        rspFlag, rsp = post_data(data)
        if rspFlag:
            rsp_json = rsp.json()
            print(rsp_json)

    except Exception as e:
        print(f'try except info: {e.args}')


def send_sms_mini_batch(sms_content, original_addr, dest_msisdns, country_codes, route_id, auth_key):
    '''
    单独发送一小批短信，短信内容唯一
    批次量限制多大，请咨询CloudSMS人员
    唯一区别是：调用该接口，只需post一次数据，就可以发送一批短信。
    :param sms_content: 短信内容
    :param original_addr: 也称OA或SenderID
    :param dest_msisdns: 目标手机号码（不含区号）, 如 [67657441,62107007]
    :param country_codes: 目标手机号码区号， 如 [852, 852]
    :param route_id: CloudSMS业务通道，由CloudSMS管理人员配置具体策略生成。
    :param auth_key: CloudSMS租户识别码，由CloudSMS管理人员配置具体策略生成。
    :return:
    '''
    try:
        multi_msisdn_list = []
        for da, country_code in zip(dest_msisdns, country_codes):
            multi_msisdn_list.append({"DEST_MSISDN": str(da), "COUNTRY_CODE": int(country_code)})

        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = {
            "METHOD": "SMS_SEND_REQUEST",
            "TYPE": "REQUEST",
            "SERIAL": 1,
            "TIME": local_time,
            "AUTH_KEY": auth_key,  # 租户的AUTH_KEY
            "ROUTE_ID": route_id,  # 业务通道Route_id
            "PRIORITY": 0,
            # "SIGNATURE": tem,
            # "SIGNATURE_TYPE": 1,
            "VERSION": "2021-01-01",
            "SMS_CONTENT": sms_content,
            "ORIGINAL_ADDR": original_addr,
            "MULTI_MSISDN_LIST": multi_msisdn_list,
        }

        rspFlag, rsp = post_data(data)

    except Exception as e:
        print(f'try except info: {e.args}')



if __name__ == "__main__":
    # country_code= 66
    country_code= None
    # country_code=852
    # dest_msisdn= 628111561606
    dest_msisdn= 85212345678
    # dest_msisdn=61400196684
    # dest_msisdn=61406586784
    # original_addr = '8612306'
    original_addr = "27hcloud"
    # sms_content = "【】메이저//안내신규+**,***승/옵OK 단/폴*처음 **%인증-코드=****le-(s)(p)(o)*.com완전최고"
    # sms_content = "메이저//안내\n신규+**,***\n승/옵OK 단/폴*\n처음 **%\n인증-코드=****\nle-(s)(p)(o)*.com완전최고"
    # sms_content = "메이저//안내\r\n신규+**,***\r\n승/옵OK 단/폴*\r\n처음 **%\r\n인증-코드=****\r\nle-(s)(p)(o)*.com완전최고"
    # sms_content = "//空签七十零a啊\r\n+**,***\r\n승/OK 단/폴*\r\n처음 **%\r\n인코드=****\r\nle-(s)(p)(o)*.com완전최고"
    # sms_content = "Your OTP is 197525. Use it within 5 minutes before it expires. "
    # sms_content = "Your Verification Code: 000000. Please do not disclose this code to anyone."
    # sms_content = "Dear All,Thank you for signing up naaHMthVIa. Please check the verification code below to verify your phone.374743 contact support@ouitrust.com."

    # sms_content = "Super Monday: The second pizza for only CHF 1.1! Great start into the week! ONLY DELIVERY. dompizza.co/*qgmTr -Text \"STOP\" to 92024"
    # sms_content = "วัน น ี ้คุณดว ง ดีได้รับทอ งค ำฟร ีๆ ขอบพระคุณที่ท่านร่วมกิจกรรมเมืองไทยสไมล์คลับ โปรดให้คะแนนความพึงพอใจเพื่อการพัฒนาที่ดียิ่งขึ้น คลิก aws2.link/fZxiLH"
    # sms_content = '[EasyLivePlus] cGYEaHtSsp Your registration SMS verification code is 66639026401-1, The validity period is 5 minutes. Do not disclose the verification code!'
    # sms_content = "【INFO】Your Verification Code: ******. Please do not disclose this code to anyone. "
    # sms_content = "Your verification code is 888222,AFRICA 갸.입.*.먄.선.물.환전.**.만 퓨짐햔혜턖 𝙖𝙛𝟐𝟐𝟗.𝐜𝐨𝐦 갸.입.쿄.듀 𝟗𝟗𝟗"
    sms_content = "daVioTriJW is MT sms, could you reply any words for the sms, thanks. Greeting from CloudSMS CMI"
    # sms_content = "【MFS】Your queue no. is # 2001 .Confirmation of Order.Thank you for ordering from Malaysian Food Street on 01 November 2022 at 09:48. <Reminder> Please do not click on any link on this channel. This channel is solely used for notification only."
    # sms_content = "2001 is ready for collection. Please collect at Malaysian Food Street,Stall 12 - Penang Hokkien Prawn Mee. Thank you for your support! <Reminder> Please do not click on any link on this channel. This channel is solely used for notification only."
    # sms_content = "[Management Perks] Your OTP is 135112. The Code is valid for 3 minutes. <Reminder> Please do not click on any link on this channel. This channel is solely used for notification only."
    # sms_content = "[#][TikTok] rfRtZLWypc is your verification codefJpzQvK2eu3"
    # route_id = "EETL_Notification"  # CloudSMS业务通道
    # route_id = "TENCENT01_Notification"  # CloudSMS业务通道
    # route_id = None  # CloudSMS业务通道
    route_id = "RTST061_Notification"  # CloudSMS业务通道
    # route_id = "OLD2NEW_Notification"  # CloudSMS业务通道
    # auth_key = "7hUkjt5IdYvjjzRuMacKpFpdAocjgcHETXazFtB#KdA6uYEFJbXx2YIcZObr+apty6NMQgdIIqbBjqwmJlNvCg=="  # CloudSMS租户的AUTH_KEY：ami_test_01
    # auth_key = "cOUlfIimjcBgfxf5cNaiOQxAZoENQe+jh9qqiox8sCIZn4AJEHi6V1d63rx9idIF5tCkNl55P4EdfoDj+rADwg=="  # CloudSMS租户的AUTH_KEY：DEMO_CMIPB
    # auth_key = "cOUlfIimjcBgfxf5cNaiOecIhvKoplBl0vUzjVMv5ORKjORa1W3gIA#Sc3zPsXbPa0RmKLeLQdQgPC7451Gfsg=="  # Neon
    # auth_key = 'cOUlfIimjcBgfxf5cNaiOXmsfkipVsqAyo6qe0mCxGr5VZFOiB5XB8rMy+N#0AUyZrwWr9tTos6wEjuWEJHlNw=='  # cmipb_tong
    auth_key = 'M9l+6IHUz3kwiXt5qzSwY#3cSbNSBA88p9KuE91E78lNy#4IZ6hFc5NQgPnMQSiYIo#59CXpwVLyGdce6cZJrw=='  # cmipb_tong02
    # # 单独发送一条短信
    # country_code = 852
    # dest_msisdn = 91679974

    for _ in range(30000):
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        send_sms(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
        # time.sleep(1/100)

    # # 单独发送一批短信，短信内容唯一
    # # 批次量限制多大，请咨询CloudSMS人员
    # country_code = [852]*3
    # for i in trange(1000):
    #     dest_msisdn = range(67650000,67660000,1000)
    #     country_code = [852] * len(dest_msisdn)
    #     send_sms_mini_batch(sms_content, original_addr, dest_msisdn, country_code, route_id, auth_key)
    #     time.sleep(1)