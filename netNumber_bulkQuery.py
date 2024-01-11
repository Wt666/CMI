import pandas as pd
import requests
import time
import json
import urllib3
urllib3.disable_warnings()

def get_cid(telenums, printWithoutSave=False, ip='18.205.248.130', result_path = f'result@cid@{time.strftime("%Y%m%d%H%M%S", time.localtime())}.xlsx'):
    result_dict_columns = ['phoneNB', 'response_code', 'message', 'name', 'type', 'hni', 'MMC', 'MNC', 'cic', 'npdi']
    result_df = pd.DataFrame(columns=result_dict_columns) # 空df
    use_time = 0
    url = f'https://{ip}:8443/gds/cid'
    print(f'url: {url}')
    for telenum in telenums:
        result_unit_dict = {
            'phoneNB': telenum,
            'response_code': None,
            'message': None,
            "name": None,
            "type": None,
            'hni': None,
            'MMC': None,
            'MNC': None,
            "cic": None,
            "npdi": None,
        }
        data = {"e164": telenum}
        data = json.dumps(data)
        ## 发出请求
        print(f'Request post data: {data}')
        begin_time = time.time()
        rsp = requests.post(url, data, headers=headers,   verify=False).content.decode('utf-8')
        end_time = time.time()
        use_time += end_time - begin_time
        if printWithoutSave:
            print(f'Response: {rsp}')
        print('rsp time used {:.2f} ms\n'.format((end_time - begin_time) * 1000))
        # rsp = {"response_code": "0", "message": "NOERROR",
        #             "cid": {"hni": "310030", "npdi": "1", "name": "AT&T Wireless", "tel": "+16613412433",
        #                     "cic": "+100321", "type": "Mobile"}}


        ## 处理响应
        if not printWithoutSave:
            rsp = json.loads(rsp)  # loads()将str变成dict
            result_unit_dict['response_code'] = rsp.get("response_code")
            result_unit_dict['message'] = rsp.get("message")
            if rsp.get('cid'):
                cid_dict = rsp.get("cid")
                result_unit_dict['name'] = cid_dict.get("name")
                result_unit_dict['type'] = cid_dict.get("type")
                result_unit_dict['cic'] = cid_dict.get("cic")
                result_unit_dict['npdi'] = cid_dict.get("npdi")
                if cid_dict.get("hni"):
                    result_unit_dict['hni'] = cid_dict.get("hni")
                    result_unit_dict['MMC'] = cid_dict.get("hni")[:3]
                    result_unit_dict['MNC'] = cid_dict.get("hni")[3:]
                else:
                    pass
            else:
                pass
            result_unit_df = pd.DataFrame(result_unit_dict, index=[0])
            result_df = result_df.append(result_unit_df)
    if not printWithoutSave:
        result_df.to_excel(result_path, index=False)
        print(f'===== to_excel, finish, {result_path} ==== \n')
    print('rsp total time used: {:.2f} ms, phoneNBs amount:{}'.format(use_time * 1000, len(telenums)))
    print('rsp total time used avg: {:.2f} ms'.format(use_time * 1000 / len(telenums)))

def get_mnis(telenums, printWithoutSave=False, ip='18.205.248.130', result_path=f'result@mnis@{time.strftime("%Y%m%d%H%M%S", time.localtime())}.xlsx'):
    result_dict_columns = ['phoneNB', 'response_code', 'message', 'status', 'name', 'type', 'hni', 'MMC', 'MNC', 'cic', 'npdi']
    result_df = pd.DataFrame(columns=result_dict_columns)  # 空df
    use_time = 0
    url = f'https://{ip}:8443/gds/mnis'
    print(f'url: {url}')
    for telenum in telenums:
        result_unit_dict = {
            'phoneNB': telenum,
            'response_code': None,
            'message': None,
            'status': None,
            "name": None,
            "type": None,
            'hni': None,
            'MMC': None,
            'MNC': None,
            "cic": None,
            "npdi": None,
        }
        data = {"e164": telenum}
        data = json.dumps(data)
        ## 发出请求
        print(f'Request post data: {data}')
        begin_time = time.time()
        rsp = requests.post(url, data, headers=headers,
                            verify=False).content.decode('utf-8')
        end_time = time.time()
        use_time += end_time - begin_time
        if printWithoutSave:
            print(f'Response: {rsp}')
        print('rsp time used {:.2f} ms\n'.format((end_time - begin_time) * 1000))

        ## 处理响应
        if not printWithoutSave:
            rsp = json.loads(rsp)  # loads()将str变成dict
            result_unit_dict['response_code'] = rsp.get("response_code")
            result_unit_dict['message'] = rsp.get("message")
            if rsp.get('mnis'):
                mnis_dict = rsp.get("mnis")
                result_unit_dict['name'] = mnis_dict.get("name")
                result_unit_dict['type'] = mnis_dict.get("type")
                result_unit_dict['cic'] = mnis_dict.get("cic")
                result_unit_dict['status'] = mnis_dict.get("status")
                result_unit_dict['npdi'] = mnis_dict.get("npdi")
                if mnis_dict.get("hni"):
                    result_unit_dict['hni'] = mnis_dict.get("hni")
                    result_unit_dict['MMC'] = mnis_dict.get("hni")[:3]
                    result_unit_dict['MNC'] = mnis_dict.get("hni")[3:]
                else:
                    pass
            else:
                pass
            result_unit_df = pd.DataFrame(result_unit_dict, index=[0])
            result_df = result_df.append(result_unit_df)
    if not printWithoutSave:
        result_df.to_excel(result_path, index=False)
        print(f'===== to_excel, finish, {result_path} ==== \n')
    print('rsp total time used: {:.2f} ms, phoneNBs amount:{}'.format(use_time * 1000, len(telenums)))
    print('rsp total time used avg: {:.2f} ms'.format(use_time * 1000 / len(telenums)))


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
        "Content-Type": "application/json",
        # 'authorization': 'Basic chinamobile_DMwB5#vZNr',
        'authorization': 'Basic CMI_DMwB5#vZNr',
        }

    ## 两个服务器ip， 设立在美国的不同位置，访问速度可能不同，任选。
    # ip = '18.205.248.130' # Virginia 18.205.248.130 (HTTPS)
    # ip = '18.189.38.46'  # Ohio     18.189.38.46   (HTTPS)
    ip = '3.0.168.215'  # Singapore     18.189.38.46   (HTTPS)

    ## 电话号码列表
    # 直接输入列表
    telenums = ["523344333731",'522294500632','527731210193',] #, "81484331560",  "19785551212", '16613412433', "85262107007", "375336585424"
    # telenums = ["6281218398636",'6281284523262','6281140600326',] #, "81484331560",  "19785551212", '16613412433', "85262107007", "375336585424"
    # telenums = ["6282219363538",'6281140201584',] #, "81484331560",  "19785551212", '16613412433', "85262107007", "375336585424"
    # telenums = ["818036553302","818031723516"] #, "81484331560",  "19785551212", '16613412433', "85262107007", "375336585424"
    # 通过读取excel文件
    # telenums = pd.read_excel(r'phoneNBs.xlsx', dtype=str)
    # telenums = telenums['phoneNB_E164'].values.tolist()
    # telenums = set(telenums) # 当电话号码有较多重复时，可以使用该命令，但确定是集合是无序的，即顺序会乱。

    ## 调用NetNumber接口查询
    get_cid(telenums, printWithoutSave=False, ip=ip)
    # get_mnis(telenums, printWithoutSave=True, ip=ip)

    print("program done")



    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67', "Content-Type": "application/json",  'authorization': 'Basic chinamobile_DMwB5#vZNr',  }
