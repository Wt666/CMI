import numpy as np
# import pandas as p3.6
# A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# B=np.arange(0,3)
# C=range(3,20,2)
# for i in C:
#     print(i)
# print(B)
# print(C)
# from functools import reduce
#
# def add(x, y) :            # 两数相加
#     return x + y
# sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
# sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
# print(sum1)
# print(sum2)
a=[0.12,0.116,0.11,0.095,0.09,0.24]
for i in a:
    b=i*0.15
    print(b)

# wt=(lambda q,w:q+w)
# print(wt(1,222222))