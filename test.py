import requests
import time
import json
import pandas as pd
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
           "Content-Type": "application/json",
           'authority': 'tsmsportal.jegotrip.com:8087',
           'authorization': 'Basic ZXlKaGJHY2lPaUpJVXpVeE1pSXNJbWxoZENJNk1UWXlPVFF5T1RVNE1Td2laWGh3SWpveE5qSTVOVEUxT1RneGZRLmV5SjFhV1FpT2pFMk9Dd2lkSGx3WlNJNk1UQXdMQ0p6WTI5d1pTSTZleUp5YjJ4bElqb2lRMDFKUVdSdGFXNVRZMjl3WlNJc0luTnRjeUk2TVN3aWRtOXBjQ0k2TVgxOS5tNkk2eVpLTUR5OHpVUTFoTnZjZGlybTY1enV5UFd0UlUwVWFnaWlWVElnQ2ZOdXo2Qk9DNXlJUFFwMldxc2l4b1pUZDVlbHNQSnkyRnlhR1lfbUdoQTo='
           }


# # stg租户信息
# url = 'https://tsmsportal.jegotrip.com:8087/public/tenement/query'
# data = {"page": 1, "page_size": 100, "type": "", "name": ""}
# data = json.dumps(data)
# html = requests.post(url, data=data, headers=headers)
# print(html.text)
# html = json.loads(html.text)
# tene = pd.DataFrame(html["msg"]["tenement_list"])
# tene.to_excel('STG租户信息.xlsx')


# # stg 产品订购信息
# url = 'https://tsmsportal.jegotrip.com:8087/sms/order/query'
# tenement_id = 130
# data = {'order_code': "",
#         'order_state': [1, 2, 3, 4, 5],
#         'page': 1,
#         'page_size': 1000,
#         'pay_type': None,
#         'product_name': "",
#         'tenement_id': tenement_id, }
# data = json.dumps(data)
# html = requests.post(url, data=data, headers=headers)
# print(html.text)
# html = json.loads(html.text)
# tene = pd.DataFrame(html["msg"]["order_list"])
# tene.to_excel('STG租户的产品订购信息.xlsx')
#
# data = {'id': 306, 'order_code': 'CloudSMS_20210817110327', 'product_code': '0Marketing7852662631',
#         'product_name': '存量业务通道MT',
#         'surplus_num': 9, 'tenement_id': 130, 'tenement_name': '比亚迪', 'use_valid_term': 10, 'use_valid_term_unit': '月',
#         'pay_type': 1, 'total_num': 10, 'create_time': '2021-08-17 11:03:49', 'status': 1, 'order_state': 2,
#         'creator': 'cmi',
#         'warn_list': [
#             {'id': 1619, 'warning_type': 1, 'warning_threshold': 20, 'warning_unit': 1, 'is_mail': 1,
#              'is_short_message': 1,
#              'is_notice_admin': 1, 'is_notice_operate': 1, 'create_time': '2021-08-17 11:03:49'},
#             {'id': 1620, 'warning_type': 1, 'warning_threshold': 0, 'warning_unit': 2, 'is_mail': 1,
#              'is_short_message': 1,
#              'is_notice_admin': 1, 'is_notice_operate': 1, 'create_time': '2021-08-17 11:03:49'},
#             {'id': 1621, 'warning_type': 2, 'warning_threshold': 10, 'warning_unit': 3, 'is_mail': 1,
#              'is_short_message': 1,
#              'is_notice_admin': 1, 'is_notice_operate': 1, 'create_time': '2021-08-17 11:03:49'},
#             {'id': 1622, 'warning_type': 2, 'warning_threshold': 0, 'warning_unit': 3, 'is_mail': 1,
#              'is_short_message': 1,
#              'is_notice_admin': 1, 'is_notice_operate': 1, 'create_time': '2021-08-17 11:03:49'}]}

# # 查看订购短信产品详情
# url = 'https://tsmsportal.jegotrip.com:8087/sms/order/detail'
# id = 306
# data = {"id":id}
# data = json.dumps(data)
# html = requests.post(url, data=data, headers=headers)
# print(html.text)
# html = json.loads(html.text)
# tene = pd.DataFrame(html["msg"])
# tene.to_excel('STG租户的产品订购信息.xlsx')
# order_info = {'id': 306, 'order_code': 'CloudSMS_20210817110327', 'tenement_name': '比亚迪', 'product_name': '存量业务通道MT',
#         'oder_serial_number': '', 'force_reply_up': None, 'channel_code': '0Marketing78526', 'sms_type': 3,
#         'pay_type': 1, 'price_currency': 'USD', 'sale_price': 1.0, 'sms_agreement': '', 'cost_sms_type': '',
#         'total_num': 10, 'use_valid_term': 10, 'use_valid_term_unit': '月', 'start_product_valid_term': '',
#         'end_product_valid_term': '', 'is_open': 2, 'physics_channel': None, 'create_time': '2021/08/17 11:03:24',
#         'product_status': 1, 'order_state': 2, 'status': 1, 'channel_list': [
#         {'region_channel_id': 75857, 'region': '塞内加尔/Senegal', 'physics_channel': 'MZF4',
#          'create_time': '2021-04-01 19:00:33', 'status': 1, 'code': 'Test04', 'sms_type': 'VerifyCode',
#          'sms_agreement': 'smpp', 'sale_price': 0.1052},
#         {'region_channel_id': 75857, 'region': '塞内加/Senegal', 'physics_channel': 'MZF5',
#                  'create_time': '2021-04-01 19:00:33', 'status': 1, 'code': 'Test04', 'sms_type': 'VerifyCode',
#                  'sms_agreement': 'smpp', 'sale_price': 0.1052},
#
#     ]}
tenement_name = []
product_name = []
channel_code = []# 业务通道编码
channel_name = []
channel_route_id = []
regionAmount = []
rps = []
phyS = []


tene_ids = [
    127,
    126,
    125,
    124,
    122,
    119,
    115,
    112,
    111,
    110,
    109,
    108,
    106,
    105,
    103,
    98,
    97,
    96,
    95,
    94,
    93,
    92,
    91,
    90,
    89,
    88,
    87,
    86,
    85,
    84,
    83,
    82,
    81,
    80,
    79,
    78,
    77,
    76,
    75,
    74,
    71,
    60,
    59,
    58,
    56,
    55,
    46,
    45,
    43,
    41,
    36,
    35,
    29,
    26,
    25,
    23,
    22,
    17,
    9,
    7
]
for tene_id in tene_ids:
    # 查看租户的产品订购信息
    url = 'https://tsmsportal.jegotrip.com:8087/sms/order/query'
    data = {'order_code': "",
            'order_state': [1, 2, 3, 4, 5],
            'page': 1,
            'page_size': 1000,
            'pay_type': None,
            'product_name': "",
            'tenement_id': tene_id}
    data = json.dumps(data)
    html = requests.post(url, data=data, headers=headers)
    html = json.loads(html.text)
    print(html)
    order_list = html["msg"]["order_list"] # STG租户的产品订购信息
    for order in order_list:
        order_id = order['id']
        # 查看订购短信产品详情
        url = 'https://tsmsportal.jegotrip.com:8087/sms/order/detail'
        data = {"id": order_id}
        data = json.dumps(data)
        html = requests.post(url, data=data, headers=headers)
        html = json.loads(html.text)
        order_info = html["msg"]

        tenement_name.append(order_info['tenement_name'])
        product_name.append(order_info['product_name'])
        channel_code.append(order_info['channel_code']) # 业务通道编码

        # 查询业务通道
        url = 'https://tsmsportal.jegotrip.com:8087/sms/channel/query'
        data = {"page":1,"page_size":10,"name":order_info['channel_code'],"p2p_type":None}
        data = json.dumps(data)
        html = requests.post(url, data=data, headers=headers)
        html = json.loads(html.text)
        channel_info = html["msg"]['channel_list'][0]
        channel_name.append(channel_info['name'])
        channel_route_id.append(channel_info['route_id'])
        # sds = {'msg': {'total': 1, 'channel_list': [
        #     {'id': 392, 'channel_code': '0Marketing78526', 'name': 'mzf_3_Marketing_MainPtl', 'english_name': None,
        #      'sms_type': 3, 'account_name': 'cmi', 'physics_channel': None, 'p2p_type': 2, 'is_open': 2, 'is_region': 1,
        #      'operation_id': 1, 'route_id': 'mzf_3_Marketing_MainPtl', 'create_time': '2021-04-01 19:00:32',
        #      'update_time': '2021-04-01 19:00:32'}]}, 'error_code': 0, 'request': 'POST /sms/channel/query'}
        channel_list = order_info['channel_list']
        regionAmount.append(len(channel_list))
        phySet = set()
        region_phy_salePrice = []
        for channel in channel_list:
            region_phy_salePrice.append([channel['region'], channel['physics_channel'], channel['code'], channel['sale_price']])
            phySet.add(channel['physics_channel'])
        rps.append(region_phy_salePrice)
        phyS.append(phySet)


dic = {
    'tenement_name':tenement_name,
    'product_name':product_name,
    'channel_code':channel_code,
    'channel_name':channel_name,
    'channel_route_id':channel_route_id,
    'regionAmount':regionAmount,
    'rps':rps,
    'phyS':phyS
}
df = pd.DataFrame(dic)
df.to_excel('stg租户信息及订购信息_初稿.xlsx')













