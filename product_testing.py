# 记得修改业务通道id

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
from tornado.httpserver import HTTPServer

url_base = {
    # "my_test_company": "https://172.22.223.192:1815/dave/io",  # STG的公司内网访问地址
    # "my_prod_company": "https://172.22.223.98:1815/dave/io",  # prod的公司内网访问地址  备环境
    "my_prod_company": "https://cloudsms-new.jegotrip.com.cn:1815/dave/io",  # prod的公司内网访问地址
}
url = url_base["my_prod_company"]

# 测试接收电话号码
dires = {
    #
    # '852':[67657478],
    # "86": [18420665911], #,15219477228,15016316139，
    # "7": [9635554698],
    # "52": [5623466838,5623796531,4444603498,5518973424],
    # "55": [11991352696], #27999751162,11935858606,21920004267,11950166776

    # "33": [667399690,664650870,602260813,767129105],
    # "91": [8019974840,8511744610,7621894524,9818140670, 9013589565, 9631875982, 9490643107],
    # "63": [639278900926],
    # "998": [913110746],

    # "357":[96265253,97830288,99007406,96467669],
    # "1":[6473763671,6138662927,5145709955,2498785077],
    # "32":[466212822,493483563,489994250,478953902],
    # "43":[6765667401,6704020430,6503204852,69918182670],
    # "61":[423111945], #402529824,469828928,474423388,470650180
    # "49":[15792313908,1704038289,15217574232,15792313908], #Germany
    # "358":[4573457019,442922088,400663692,466598225],
    # "372":[56255267,56649527,51984723,5503661],
    # "852":[51979170, 93370260, 62794008, 55339597, 54013106,69694223,53899764,94622595],
    # "30":[6947432812,6937407936,6987458519,6946080805],
    # "353":[892211680,858210257,852837240,831611762],

    # "39":[3714733051,3472709604,3703033790,3735067588],
    # "81":[9039669408], # 9039669408,9069114613,9092913638,
    # "371":[24942141,29752263,26844808,27512710],
    # "370":[62385508,68976347,61647099,68249732],
    # "352":[661153228,621662074,661360320,691155422],
    # # "356":[79807940,77076070,79047528,99431967],
    # "65":[91443604],# 94795081,82339461,98229106
    # "351":[917970611,914375747,969605274,912533518],
    # "64":[279242143,226392210,272149545,2102249094],
    # "31":[651972469,684624052,616314361,684963939],
    # # "421":[917795903,919272635,907576578,903295664],
    # "82":[1049949079,1065354948,1022408110,1030539790], #Korea
    # # "34":[633154857,600460768,679450282,653150255],
    # "44":[7909091569,7411064545,7957557539,7774056849],
    # "1":[6613412433,7082659239,6025598356,3098268966],

    # "66":[968489252,618699662,965591696,933248237],
    "62":[8111561606], # 88806298608,85812748374, 85937060026, 83819656567,8111561606,88806298608,85812748374, 85937060026, 83819656567,83175993715,89612149632 # Indonesia
    # "375":[295996171, 333795585, 295159758, 292999863, 333047926, 292481221, 297132285, 333742882], #Belarus
    # "886":[922441271], # 979856571,973237077,926700596,933455005,906875894,989415871,982755783,905492964
    # "57":[3185212721,3207561356,3005199458,3503585204,3167613628],#
    # "57":[3041219757,3126022835,3193517137,3012048799,3057600182,3024656140],#
    # "27":[603858894,743413029,794934424,719152287], #813096206
    # "234":[9065934231,9050904100,9074880958,8034718926],#9098560115,8146417645 Nigeria
    # "853":[63151030],
    # "81":[8047889989],

    # "971":[557661788],
    # "60":[197777100,1132692256,196309646], #Malaysia
    # "856":[2077929912],
    # "673":[8373707],
    # # "95":[9453310004],
    # "84":[906287255],
    # "886":[933154426], #real number 971535056, 922441271,978716969,
    # "855":[77877477],
    # "886":[978832989,926700596,937055171,906582982],
    # "82":[1022682700],
    # "92":[3244509808,3307650035,3216837704,3006820041,3239663734],#Pakistan
    # "34":[642580342], #Spain
    # "20":[1119353306], #Egypt
    # "98":[9915944986], #Iran
    # "90":[5380680179,5536929279], #Turkey
    # "41":[789762612,779452250,772169615], #Switzerland
    # "380":[965030435,941262971,918070120], #Ukraine
    # "977":[9819398935,9849287795,9887112014], #Nepal
    # "53":[53443772,53443772,], #Cuba
    # "46":[722069635,739577358,793330014], #Sweden
    # "47":[40979191,97616795,98082691], #Norway
    # "56":[959302332,957206619,953223301], #Chile
    # "880":[1932523987,1983224431,1977004469,1999587191,1625000251,1877696492] #Bangladesh
    # "961":[79128661,70114712,76467476,70731488,78846662] #Lebanon
    # "968":[97917837,72003721,97133135,97133135,97917837] #Oman
}

# 短信模板
templs = {
    # 8种：字母OA、数字OA，长短信、短信，中文、英文
    # "852655": "【太阳锅巴】双十一倒计时，买1件送5袋，买2件送15袋，送糯米锅巴试吃装！优享不容错过！错过再等一年，速来抢 m.tb.cn/h.fHLFLb0?tk=xLD62Qy2llb 退订回N",
    # "planet": "「まだ受け取ってないの学園」ご入学おめでとうございます！http://c*sm*a.com/RjY*L*X",
    # "106575864009": "铳 剁 玿 颂 剁 玿 tbtybet23.vip:1234",
    # "Google": "【GTKVN-VPN】Your verification code is 123456,valid for 1 minute.",
    # "234567": "Your pin code is 111111, please do not disclose it, if you have any question, please contact me, as the M800 cannot provide service, Vietnam is left empty, so I do not pick up your phone call,  best regard.",

    # "61485836472": "Your pin code is 111111, please do not disclose it.",
    # "DanaRupiah": "Congratulations King! We are pleased to inform you that you have been selected and eligible to purchase WTAPS 1234 SS COLLECTION. Please follow below instructions to secure your purchase eligibility. Each customer can purchase a maximum of 2 item per style only. T&C apply.Queue Ticket Number: 2Date: 11 JUNE 1111Time: 11:11AMShop Location: HOODS STORE HONG KONG (Shop C, 22 Ice House Street, Central)",
    # "dloudSMS": "您的一次性验证码为 111111 ,请勿告知他人,谢谢。[今日知识]知识就像海洋，只有意志坚强的人才能到达彼岸。这是伟大的马克思的名言名句，送予意志坚强的你，希望继续坚持，早日登上理想的彼岸，regrads.",
    # "456789": "您的一次性验证码为 111111 ,请勿告知他人,谢谢。[今日知识]知识就像海洋，只有意志坚强的人才能到达彼岸。这是伟大的马克思的名言名句，送予意志坚强的你，希望继续坚持，早日登上理想的彼岸，regrads.",
    #
    # "886960299366": "我是昨天給您打過電話的陳小姐 有些事沒跟您說清楚 麻煩您添加我ID：12345678",
    # "DanaRupiah": "Your pin code is 111111, please do not disclose it, if you have any question, please contact me, as the M800 cannot provide service, Vietnam is left empty, so I do not pick up your phone call,  best regard.",
    "DanaRupiah": "[DanaRupiah]Your pin code is 111111, please do not disclose it.",
    # "222": "Your pin code is 111111, please do not disclose it, if you have any question, please contact me, as the M800 cannot provide service, Vietnam is left empty, so I do not pick up your phone call,  best regard.",
    # "CCC": "您的注册验证码为：111111",
    # "333": "您的验证码是111111。请注意保护您的验证码信息，不要分享给其他人。",
    # "DDD": "您的一次性验证码为 111111 ,请勿告知他人,谢谢。[今日知识]知识就像海洋，只有意志坚强的人才能到达彼岸。这是伟大的马克思的名言名句，送予意志坚强的你，希望继续坚持，早日登上理想的彼岸，regrads.",
    # "444": "您的一次性验证码为 111111 ,请勿告知他人,谢谢。[今日知识]知识就像海洋，只有意志坚强的人才能到达彼岸。这是伟大的马克思的名言名句，送予意志坚强的你，希望继续坚持，早日登上理想的彼岸，regrads.",

    # "886960235366": "TCDC_Notification",
    # "123456": "Your verification code is 111111",
    # "Google": "Your pin code is 111111, please do not disclose it, if you have any question, please contact me, as the M800 cannot provide service, Vietnam is left empty, so I do not pick up your phone call,  best regard.",
    # "234567": "Your pin code is 111111, please do not disclose it, if you have any question, please contact me, as the M800 cannot provide service, Vietnam is left empty, so I do not pick up your phone call,  best regard.",
    #
    # "Moment ": "口座情報をご確認後、開始させていただきますhttp://ola***.com/*R*hLfSjxy",
    # "Moment": "あなた様のお口座へこれより開始となりますhttp://ola***.com/XHz*DK*so",
    # "CloudSMS": "Kode pin Anda 111111, tolong jangan mengungkapkannya.",
    # "CloudSMS": "【INFO】 您的大盤平台短信验证码为123456，有效期为01分钟",
    # "WEBSMS": "Parabens, voce foi selecionado para este trabalho. Mais de 022R. Aceite esta vaga https://bit.ly/099kFhO",
    # "CloudSMS": "[INFO] 您的kolcity平台短信验证码为213456，有效期为03分钟",
    # "FIRE": "驗證碼：745732，請及時驗證，遞送1小时内",
    # "BITC": "驗證碼：111111，請及時驗證，如非本人操作，請忽略本短信。111",
    # "BITC": "驗證碼：745732，請及時驗證，如非本人操作，請忽略本短信。222",
    # "Moment": "川崎栄一様　ご入金に関する重要通知で御座いますhttp://ola***.com/cHfzFbw",
    # "Moment": "【スマホのみの副業/副収入/完全限定配信】LINE無料友だち登録で全部教えます！http://r**s.com/hKd*O"
}

def save_file(file_name, data, rsp):
    with open(file_name, "a") as f:
        f.write("\nRequest Data: \n")
        f.write(data)
        f.write("\nRespond Data: \n")
        f.write(rsp)

def get_sms_wait():
    '''生成短信等待发送批次
    sms_wait = {div: [dire, sms_oa, sms_ctn, phone]}
    '''
    sms_wait = {}
    for i, templ in enumerate(templs.items()):
        for dire, phones in dires.items():
            div, mod = divmod(i, len(phones))
            if sms_wait.get(div):
                sms_wait[div].append([dire, templ[0], templ[1], phones[mod]]) # templ[0]
            else:
                sms_wait[div] = []
                sms_wait[div].append([dire, templ[0], templ[1], phones[mod]])
    return sms_wait

def post_and_resp(data):
    data = json.dumps(data)
    print("\n请求数据包:\n{}".format(data))
    rsp = requests.post(
        url, data, verify=False).content.decode('utf-8')
    print("响应数据包:\n{}".format(rsp))

    # 保存发送记录
    rsp_new = json.loads(rsp)
    code = rsp_new["RESULT_CODE"]
    # 发送成功的记录（保存为两个文件）
    if code != 1:
        print("发送异常:")
        print(f'sms_oa:{sms_oa}')
        print(f'cc:{dire}, phone:{phone}')
        save_file(file_name="STG_Fail.txt",
                  data=data, rsp=rsp)

def sms_send():
    try:
        had_sent = 0
        sms_wait = get_sms_wait()
        sms_amount = len(dires) * len(templs) # 短信发送总量 == 国家方向个数 * 短信模板数(8)
        print("此次产品测试短信总发送量应为：{}条".format(sms_amount))
        print(f"分成{len(sms_wait)}个批次发送，每个批次发送后休眠5分钟")
        for bulks in sms_wait.values():
            for bulk in bulks:
                local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                data = {
                    "METHOD": "SMS_SEND_REQUEST",
                    "TYPE": "REQUEST",
                    "SERIAL": 1,
                    "TIME": local_time,
                    "AUTH_KEY": "cOUlfIimjcBgfxf5cNaiOVRjhQfJj1FIIj3FXGRJnwLVkkAe#jiT4n96f8#eCpKN3vvnauinWCqZK4WrpRGpAw==", # 租户的AUTH_KEY

                    "ROUTE_ID": "WT_Notification_120",  # 业务通道Route_id
                    "PRIORITY": 0,
                    # "SIGNATURE_TYPE": 1,
                    "VERSION": "2020-07-12",
                    "SMS_CONTENT": bulk[2],
                    "ORIGINAL_ADDR": bulk[1],
                    # "SIGNATURE": "tem",
                    "MULTI_MSISDN_LIST": [{"DEST_MSISDN": str(bulk[3]),
                                           "COUNTRY_CODE": int(bulk[0])}],
                }
                post_and_resp(data)
                had_sent += 1
            if 0 < sms_amount - had_sent:
                print(f"已发送{had_sent}条短信，剩余{sms_amount - had_sent}条等待发送。")
                time.sleep(300)  # 号码休眠，降低运营商屏蔽号码的几率
            else:
                print(f"发送完毕。已发送{had_sent}条短信")
    except Exception as e:
        print("发送失败")
        print(e.args)
        print(str(e))
        print(repr(e))
    # print(结束)

# class IndexHandler(tornado.web.RequestHandler):
#     def post(self):
#         jsonbyte = self.request.body
#         jsonstr = jsonbyte.decode('utf-8')
#         print(jsonstr)

if __name__ == "__main__":
    print("program begin.")
    sms_send()
    print("program done.")



    # app = tornado.web.Application(
    #     [(r'/', IndexHandler)], static_path='static', debug=True, autoreload=False)
    # app.listen(59999)
    # tornado.ioloop.IOLoop.instance().start()


