#! /usr/bin/env python3
# coding:utf-8
import unittest
def main():
    reg_content = '''
พนัน
กู้
สินเชื่อ
เงินทุน
อนุมัติไว
รายได้
สมัครเงิน
เงินด่วน
อนุมัติเร็ว
เครดิต
ค้ำประกัน
หนี้
รับเงิน
รางวัล
ลุ้น
ดวง
โชค
รวย
หวย
แจ็คพอต
แจคพอต
สล็อต
สลอต
คาสิโนสินเชื่อ
สมัครเงิน
อนุมัติเร็ว
คาสิโน
พ  นัน
กู้
สิ นเ ชื่อ
เงิ นทุ น
อนุมัติไ ว
รายได ้
สมัค รเงิน
เงินด ่วน
อนุมัต ิเร ็ว
เครด ิต
ค ้ำ ปร ะกัน
หน ี้
รับเง ิน
รางว ัล
ล ุ้น
ด วง
โช ค
รว ย
หว ย
แจ ็คพอต
แจค พอต
สล ็อต
สล อต
คาส ิโน
ดวงดี ได้รับ
'''
    sms_content = "[THLIVE] ยรหัสยืนยันการลงทะเบียน：****ใช้ได้ภายใน * นาที"
    for reg in reg_content.split("\n"):
        if reg in sms_content:
            print(reg)

if __name__ == "__main__":
    main()
# if __name__ == '__main__':
    unittest.main()
# import requests
# url = 'http://localhost:8887/BYTE01'
# rsp = requests.post(url, {"greeting":'AAA'}, verify=False)
# print(rsp)
# print(rsp.text)