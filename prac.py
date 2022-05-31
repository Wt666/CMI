from unittest import result
import numpy as np
import pandas as pd
import time
a=[[1],[3],[99],[62],[34],[0.1]]
def Sort(x):
    print('start')
    n=len(x)
    if n<=1:
        return x
    for i in range (0,n):
        for j in range(0,n-i-1):
            if x[j]>x[j+1]:
                (x[j],x[j+1])=(x[j+1],x[j])
    print('end')
    return x
time=time.perf_counter()
result=Sort(a)
for q in result:
    index=a.index(q)
b=[]
b=b.append(index)
print(b)
print(result)
print(time)





