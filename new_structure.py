import pandas as pd
import numpy as np
import xlwt

df = pd.read_excel("sms_router_cfg.xlsx")
# print(df)
# df1.to_csv
list1=[]
for i in df['sms_route_json']:
    list1.append(i)
    # print(i)
    print(list1)
# df3=pd.DataFrame(list)
# print(df3)
# print(list(i))
def export_excel(export):
    #将字典列表转换为DataFrame
    pf = pd.DataFrame(export)
    print(pf)
    #指定字段顺序
    order = ['ROUTE_ID','ALIAS','SMS_TYPE','OPER_TYPE','OBJECT','COMM_TYPE']
    pf = pf[order]
    columns_map={
        'ROUTE_ID':'a', 'ALIAS':'b', 'SMS_TYPE':'c', 'OPER_TYPE':'d', 'OBJECT':'e', 'COMM_TYPE':'f'
    }
    pf.rename(columns=columns_map, inplace=True)
    file_path = pd.ExcelWriter('/Users/wt/Documents/配置文档/testnew.xlsx')
    # 输出
    pf.fillna(' ', inplace=True)
    pf.to_excel(file_path, encoding='utf-8', index=False)

    file_path.save()

if __name__ == '__main__':
    #将分析完成的列表导出为excel表格
    export_excel(list1)

    # ['OBJECT']['ISP_LIST']['PTL_LIST']['PTL_NAME']

# {"ROUTE_ID": "wuyouxing_VerifyCode_to_alisms",
#  "ALIAS": "wuyouxing_VerifyCode_to_alisms",
#  "SMS_TYPE": "VerifyCode",
#  "OPER_TYPE": "UPDATE",
#  "OBJECT": [{"OBJECT_NAME": "default",
#              "OBJECT_TYPE": "Undirect",
#              "ISP_LIST": [{"ISP_NAME": "default",
#                            "PTL_LIST": [{"PTL_NAME": "BOSSCMI1",
#                                          "SCORE": 0.5},
#                                         {"PTL_NAME": "BOSSCMI2",
#                                          "SCORE": 0.5}]}]}],
#  "COMM_TYPE": "MT"}
