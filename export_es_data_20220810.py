# ! /usr/bin/env python3
# coding:utf-8

import codecs
import os
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch import helpers
import json
import time

day = time.strftime("%Y-%m-%d", time.localtime())

def search_es(tenantName, es_client, page, page_size, sort_field=None, is_sort=None):
    index_name = "jegom_sms"
    query = {
        "query": {
            "bool": {
                "filter": [
                    {
                        "range": {
                            "RecvTime": {
                                # "gte": "2022-08-23T09:00:00Z",
                                # "lte": "2022-08-24T08:59:59Z",

                                "gte": "2022-08-24T00:00:00Z",
                                "lte": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime()),


                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "TenantName": tenantName
                        }
                    }
                ]
            }
        },
        "track_total_hits": True,
        "sort": [
            {
                "RecvTime": {
                    "order": "desc"
                }
            }
        ]
    }
    query_body = query
    if page and page_size and is_sort:
        query_body["sort"] = [{
            sort_field: {
                "order": "desc"
            }
        }]
    print("query_body:{0}".format(query_body))
    if page and page_size:
        from_page = int(page_size) * (int(page) - 1)
        result = es_client.search(index=index_name,
                                  body=query_body,
                                  timeout='1m',
                                  size=page_size,
                                  from_=from_page,
                                  sort=sort_field)
    else:
        result = es_client.search(index=index_name,
                                  body=query_body,
                                  scroll="50m",
                                  timeout='1m',
                                  size=100)
    return result


def data_serialize(tenantName, es_client, page=None, page_size=None, sort_field=None, is_sort=None):
    data = search_es(tenantName, es_client, page, page_size, sort_field, is_sort)
    if 'error' in data:
        # es搜索报错
        return False, [], 0
    hits = data["hits"]
    rows = hits.get('hits', [])
    if not rows:
        print('Response::empty')
        return True, [], 0
    total = hits['total']['value']
    if "_scroll_id" in data:
        scroll_id = data["_scroll_id"]  # 游标id
        print('total:{0},scroll_id:{1}'.format(total, scroll_id.strip()))
        print('page:{}，total:{}-'.format(0, len(rows)))
        for i in range(int(total / 100)):
            res = es_client.scroll(scroll_id=scroll_id, scroll='50m')
            rows = rows + res["hits"]["hits"]
            print('page:{}，total:{}-'.format(i + 1, len(rows)))
    return True, rows, total



def main():
    # tenantName = 'BYTE_PK03_SMPP'
    # tenantName = 'BIGO_SMPP01'
    tenantName = 'CMIPB'
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("base_dir:{0}".format(base_dir))
    url = 'http://172.22.223.56:9200/'
    es_client = Elasticsearch(url)
    flag, rows, total = data_serialize(tenantName,es_client, page=None, page_size=None, sort_field=None, is_sort=None)
    print(flag, len(rows), total)
    result = ""
    es_data_list = []
    for es_line_dic in rows:
        print(es_line_dic)
        tmp_dic = {}
        _source_dic = es_line_dic["_source"]
        tmp_dic["Country Code"] = _source_dic["CountryCode"]
        tmp_dic["Phone Number"] = _source_dic["DestMsisdn"]
        # tmp_dic["SendTime"] = _source_dic["SendTime"]
        # tmp_dic["RecvTime"] = _source_dic["RecvTime"]
        tmp_dic["SenderID"] = _source_dic["SourceMsisdn"]
        # tmp_dic["SMS Content"] =_source_dic["Content"]
        tmp_dic["UID"] = _source_dic["sms_uuid"]
        tmp_dic["Route ID"] = _source_dic["RouteID"]
        tmp_dic["SMS Status"] = _source_dic["Status"]
        tmp_dic["DR State"] = _source_dic["Report"]
        tmp_dic["ReportCode"] = _source_dic["ReportCode"]
        tmp_dic["Segment Quantity"] = _source_dic["SMPP_STANDARD"]
        tmp_dic["CountryCode"] = _source_dic["CountryCode"]
        tmp_dic["ES_RecvTime"] = _source_dic["RecvTime"][:-1].replace('T', ' ')
        tmp_dic["ES_SendTime"] = _source_dic["SendTime"][:-1].replace('T', ' ')
        tmp_dic["ES_RespondTime"] = _source_dic["RespondTime"][:-1].replace('T', ' ')
        tmp_dic["ES_ReportTime"] = _source_dic["ReportTime"][:-1].replace('T', ' ')
        # tmp_dic["Conversion_Rate"] = _source_dic["Conversion_Rate"]
        if "Conversion_Rate" in _source_dic.keys():
            tmp_dic["CR"] = 1
        else:
            tmp_dic["CR"] = 0
        if _source_dic["ReportCode"] == 'DELIVERED':
            tmp_dic["DLRED"] = 1
        else:
            tmp_dic["DLRED"] = 0
        if _source_dic["SourceMsisdn"] == 'TikTok':
            tmp_dic["isTikTokOA"] = 'TikTok'
        else:
            tmp_dic["isTikTokOA"] = 'ElseOA'
        # tmp_dic["IspName"] = _source_dic["IspName"]
        isp_dict = {
            'CMPak_Limited_kGWjFi7iU7eJAIlBGgdWmw': 'CMPak',
            'Pakistan_Telecommunication_Mobile_Lim_WEzGREbEhhuFu1ncHuOUyQ': 'PTM(Ufone)',
            'Telenor_Pakistan_Private_Limited_9uLDK3vVFpnTnNRb210_rg': 'Telenor',
            # 'Pakistan_Mobile_Communications_Limite_yWC31Jy0KICbeMxIQVYdsw': 'PMCL-Jazz/waridTel(mnc:07)',
            'Pakistan_Mobile_Communications_Limite_yWC31Jy0KICbeMxIQVYdsw': 'PMCL-waridTel(mnc:07)',
            'Pakistan_Mobile_Communications_Limite_ZxScFK3qzjOahkKO_zlijQ': 'PMCL-Mobilink(mnc:01)',
        }
        tmp_dic["IspName"] = isp_dict.get(_source_dic["IspName"], _source_dic["IspName"])
        tmp_dic["Content"] = _source_dic["Content"]
        tmp_dic["DestProtocol"] = _source_dic["DestProtocol"]
        tmp_dic["coding"] = _source_dic["coding"]
        es_data_list.append(tmp_dic)

    pf = pd.DataFrame(es_data_list)
    pf.to_csv(f"{tenantName}_{day}_{time.time()}.csv", index=False)
    print('len of ', pf.shape)

    # gb1 = pf.groupby(["isTikTokOA","IspName", "DestProtocol"]).size()
    # gb2 = pf.groupby(["isTikTokOA","IspName", "DestProtocol"])['CR'].sum()

if __name__ == "__main__":
    main()
