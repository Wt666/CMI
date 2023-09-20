import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def dict_to_excel(data_dict, file_name):
    # 将字典转换为DataFrame
    df = pd.DataFrame.from_dict(data_dict, orient='index')
    # 创建一个Excel工作簿
    wb = Workbook()
    # 选择第一个工作表
    ws = wb.active
    # 将DataFrame中的数据写入工作表
    for r in dataframe_to_rows(df, index=True, header=True):
        ws.append(r)
    # 保存Excel文件
    wb.save(file_name)


# 示例数据字典
data_dict = {"CNY": 1, "AED": 0.534, "AFN": 12.44, "ALL": 14.87, "AMD": 56.21, "ANG": 0.26, "AOA": 74.35,
                       "ARS": 31.62, "AUD": 0.216, "AWG": 0.26, "AZN": 0.247, "BAM": 0.259, "BBD": 0.291, "BDT": 15.42,
                       "BGN": 0.259, "BHD": 0.0547, "BIF": 302.58, "BMD": 0.145, "BND": 0.194, "BOB": 1.01,
                       "BRL": 0.737, "BSD": 0.145, "BTN": 11.94, "BWP": 1.91, "BYN": 0.388, "BZD": 0.291, "CAD": 0.196,
                       "CDF": 302.58, "CHF": 0.13, "CLP": 115.4, "COP": 656.96, "CRC": 77.63, "CUP": 3.49, "CVE": 14.61,
                       "CZK": 3.11, "DJF": 25.83, "DKK": 0.989, "DOP": 7.95, "DZD": 19.72, "EGP": 4.49, "ERN": 2.18,
                       "ETB": 7.91, "EUR": 0.133, "FJD": 0.322, "FKP": 0.117, "FOK": 0.989, "GBP": 0.117, "GEL": 0.364,
                       "GGP": 0.117, "GHS": 1.73, "GIP": 0.117, "GMD": 9.27, "GNF": 1235.53, "GTQ": 1.13, "GYD": 30.72,
                       "HKD": 1.14, "HNL": 3.57, "HRK": 0.998, "HTG": 22.67, "HUF": 50, "IDR": 2157.41, "ILS": 0.531,
                       "IMP": 0.117, "INR": 11.94, "IQD": 191.72, "IRR": 6172.59, "ISK": 19.8, "JEP": 0.117,
                       "JMD": 22.21, "JOD": 0.103, "JPY": 19.52, "KES": 19.65, "KGS": 12.72, "KHR": 593.05,
                       "KID": 0.216, "KMF": 65.19, "KRW": 192.46, "KWD": 0.0445, "KYD": 0.121, "KZT": 66.33,
                       "LAK": 2477.05, "LBP": 2180.42, "LKR": 46.59, "LRD": 23.7, "LSL": 2.63, "LYD": 0.692,
                       "MAD": 1.47, "MDL": 2.62, "MGA": 640.12, "MKD": 8.19, "MMK": 342.65, "MNT": 505.44, "MOP": 1.17,
                       "MRU": 4.98, "MUR": 6.54, "MVR": 2.24, "MWK": 150.03, "MXN": 2.62, "MYR": 0.645, "MZN": 9.29,
                       "NAD": 2.63, "NGN": 66.88, "NIO": 5.31, "NOK": 1.54, "NPR": 19.1, "NZD": 0.235, "OMR": 0.0559,
                       "PAB": 0.145, "PEN": 0.548, "PGK": 0.512, "PHP": 8.15, "PKR": 41.2, "PLN": 0.61, "PYG": 1034.98,
                       "QAR": 0.529, "RON": 0.653, "RSD": 15.55, "RUB": 11.85, "RWF": 167.52, "SAR": 0.545, "SBD": 1.2,
                       "SCR": 1.9, "SDG": 64.93, "SEK": 1.5, "SGD": 0.194, "SHP": 0.117, "SLE": 3.29, "SLL": 3288.5,
                       "SOS": 82.52, "SRD": 5.35, "SSP": 125.04, "STN": 3.25, "SYP": 365.12, "SZL": 2.63, "THB": 4.99,
                       "TJS": 1.58, "TMT": 0.509, "TND": 0.431, "TOP": 0.342, "TRY": 2.82, "TTD": 0.988, "TVD": 0.216,
                       "TWD": 4.45, "TZS": 341.14, "UAH": 5.36, "UGX": 542.99, "USD": 0.145, "UYU": 5.66, "UZS": 1653.5,
                       "VES": 3.58, "VND": 3419.8, "VUV": 17.16, "WST": 0.396, "XAF": 86.92, "XCD": 0.392, "XDR": 0.108,
                       "XOF": 86.92, "XPF": 15.81, "YER": 36.37, "ZAR": 2.63, "ZMW": 2.52, "ZWL": 144.07}

# 将数据字典写入Excel文件
dict_to_excel(data_dict, 'output1.xlsx')
