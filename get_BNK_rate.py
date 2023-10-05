import time
import requests
from urllib.parse import urlencode
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
pd.set_option('display.width',120)
# 精度要求
# pd.set_option('precision',3)
np.set_printoptions(precision=3)
pd.set_option('display.float_format', lambda x: '%.3f' % x)



url = 'https://srh.bankofchina.com/search/whpj/search_cn.jsp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'srh.bankofchina.com',
    'Origin': 'https://srh.bankofchina.com',
    'Referer': 'https://srh.bankofchina.com/search/whpj/search_cn.jsp',  # 通用文字识别接口，高精度不带位置
    # # '':'',
}
data = {
    'erectDate': '',  # 起始时间，如2023-08-01
    'nothing': '',  # 结束时间
    'pjname': '港币',
    # 'page': 2,
    'head': 'head_620.js',
    'bottom': 'bottom_591.js',
}
data = urlencode(data)

def get_rate():
    html = requests.post(url, data, headers=headers)
    # print(html)
    df_list = pd.read_html(html.text)[1]
    df_list = df_list.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1).dropna()
    df_list = df_list.dropna()
    # print(df_list)
    # df_list.to_excel(f'./rate/{time.time()}.xlsx')
    print(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
          f" CR_rolling:{df_list['现汇买入价'][0]}, {df_list['现汇卖出价'][0]}, [{min(df_list['现汇买入价'])}, {max(df_list['现汇买入价'])}]")
    return df_list

def plot_buying_rate():
    pf = get_rate()
    buying_rate = pf['现汇买入价'].to_list()[::-1]
    selling_rate = pf['现汇卖出价'].to_list()[::-1]
    release_time = pf['发布时间'][0]
    while True:
        try:
            plt.plot(buying_rate, '--b.')[0]
            plt.plot(selling_rate, '--r.')[0]
            # if pf['CR_rolling1000'][-1] < 0.505:
            #     send_alert_email(f"最近期的1000条短信CR为{pf['CR_rolling1000'][-1]}")
            # 这个就是表的刷新时间了，以秒为单位
            plt.pause(30)
            pf = get_rate()
            if pf['发布时间'][0] == release_time:
                continue
            else:
                buying_rate.append(pf['现汇买入价'][0])
                selling_rate.append(pf['现汇卖出价'][0])
                release_time = pf['发布时间'][0]
                print(f'min:{min(buying_rate)}, max:{max(buying_rate)}, max:{max(selling_rate)}')
        except Exception as e:
            time.sleep(3600)

def lastly1000per5min():
    fig = plt.figure()
    window = 200
    plt.title(f'CMPAK_CR_rolling{window}')
    plt.grid(True)
    line = None  # 给定一个参数，用来标识是不是第一次创建

    while True:
        pf = get_rate()
        yv = pf['现汇买入价'].to_list()[::-1]
        # 如果图还没有画，则创建一个画图
        if line is None:
            # -代表用横线画，g代表线的颜色是绿色，.代表，画图的关键点，用点代替。也可以用*，代表关键点为五角星
            line = plt.plot(yv, '--b.', marker='.')[0]

        # 这里插入需要画图的参数，由于图线，是由很多个点组成的，所以这里需要的是一个列表
        # line.set_xdata(pf['发布时间'])
        line.set_ydata(yv)

        print(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"), f"{pf.shape[0]}__CR_rolling:", yv[-1])
        # if pf['CR_rolling1000'][-1] < 0.505:
        #     send_alert_email(f"最近期的1000条短信CR为{pf['CR_rolling1000'][-1]}")
        # 这个就是表的刷新时间了，以秒为单位
        plt.pause(1 * 60)



if __name__ == '__main__':
    plot_buying_rate()