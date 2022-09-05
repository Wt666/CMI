import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from datetime import *
# from datetime import datetime, date, time, timedelta
from portal_operation_uip import *


def get_dispatchingLog_DF(start_date, end_date, tenant_id, country_code=None, msisdn=None, uid=None):
    # 27 是 CMIPB
    # start_date = "2021-10-27 00:00:00",
    # end_date = "2021-10-27 23:59:59",
    # start_date = str(datetime.combine(date.today() - timedelta(days=1), time.min)),
    # end_date = str(datetime.combine(date.today(), time.max)),
    # 根据租户id，查询发送记录
    url = 'https://smsportal.jegotrip.com:8087/sms/stat/record'
    data = {"page": 1, "page_size": 1, "start_date": start_date, "end_date": end_date,
            "tenement_id": tenant_id, "country_code": country_code, "msisdn": msisdn, "status": "", "uid": uid}
    data = json.dumps(data)
    html = requests.post(url, data=data, headers=HEADERS_PORTAL)
    print(html.text)
    html = json.loads(html.text)
    dispatching_Df = pd.DataFrame(html["data"]["data"])
    # print(dispatching_Df)
    # print(f'len of dispatchingLog_DF: {len(dispatching_Df)}')
    return dispatching_Df


def analy_dispatchingLog(start_date, end_date, tenant_name="CMIPB", country_code=None, msisdn=None):
    if tenant_name == "CMIPB":
        tenant_id = 27
    elif tenant_name == 'BIGF':
        tenant_id = 5
    else:
        tenant_id = get_tenant_id(tenant_name)
    dispatchingLog_DF = get_dispatchingLog_DF(
        start_date, end_date, tenant_id, country_code, msisdn)
    print(f'{tenant_name}: From {start_date} To {end_date}: ')
    print(f'len of dispatchingLog_DF: {len(dispatchingLog_DF)}')
    gb1 = dispatchingLog_DF.groupby(["status", "report_code"]).size()
    gb2 = gb1 / len(dispatchingLog_DF)
    pdc = pd.concat([gb1, gb2], axis=1)
    pdc.columns = ['size', 'ratio']
    print(pdc)


if __name__ == "__main__":
    start_date = '2021-12-02 00:00:00'
    end_date = '2021-12-02 23:59:59'
    tenant_name = "BIGF"
    # start_date = str(datetime.combine(
    #     date.today() - timedelta(days=1), datetime.time.min))
    # end_date = str(datetime.combine(date.today(), datetime.time.max))
    print(f'{tenant_name}: From {start_date} To {end_date}: ')
    df = get_dispatchingLog_DF(start_date, end_date,
                               tenant_id=get_tenant_id(tenant_name))
    print(df["status"].values[0])
    # analy_dispatchingLog(start_date, end_date, tenant_name)
    print('program done.')

    # #
    # dispatchingLog_DF['send_time'] = pd.to_datetime(dispatchingLog_DF['send_time'])
    # dispatchingLog_DF['report_date'] = pd.to_datetime(dispatchingLog_DF['report_date'])
    # # dispatchingLog_DF = dispatchingLog_DF.set_index('send_time')
    # dispatchingLog_DF = dispatchingLog_DF[['failure_cause', 'msisdn', 'proposal', 'report_code', 'report_date', 'route_id', 'send_time',
    #    'source_msisdn', 'status', ]]
    #
    # dispatchingLog_DF['report_date'] < pd.to_datetime('2021-11-08 16:13:18')
    #
    # from datetime import timedelta
    # min_time = dispatchingLog_DF['send_time'].min() # Timestamp('2021-11-08 14:52:03')
    # # dispatchingLog_DF[dispatchingLog_DF[]]
    # dt1 = pd.to_datetime('2021-11-08 16:12:57') + timedelta(seconds=5)
    # dt2 = pd.to_datetime('2021-11-08 16:12:50')
    # #
