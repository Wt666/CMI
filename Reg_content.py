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
ly/5IEb
https://t.ly/5IEb
https://o.roopcn.com
แอดไลน์ :0967427422 ได้10000-100000
'''
    sms_content = "END OF SEASON SALE **% OFF ON SELECTED ITEMS * JAN - ** JAN ** at OUR STORES OR CLICK https://bit.ly/*aB*nyg"
    for reg in reg_content.split("\n"):
        if reg in sms_content:
            print(reg)
if __name__ == "__main__":
    main()
# if __name__ == '__main__':
    unittest.main()

