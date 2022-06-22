import pandas as pd
import numpy as np
Path="a.csv"
data1= {
    "name":["WT","WTT"],"age":[10,20]
}
data2={
    "name":["A","B","C"],"age":[22,33,44]
}
df1=pd.DataFrame(data=data1)
df2=pd.DataFrame(data=data2)
df3=df1.merge(df2,how='outer')
df4=pd.concat([df1,df2],sort=True)
# df.to_csv(Path,index=False)
print(df3)
print(df4)
a="miscellaneous"
print(str.upper(a))
# S1=pd.Series(['a','b'])
# S2=pd.Series(['c','d'])
# print(pd.concat([S1,S2],ignore_index=True))
# print(df2)
# print(df.pivot(index='age',columns='name'))