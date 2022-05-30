# import pandas as pd
# import numpy as np
# # Create DataFrame from multiple lists
# technologies =  ['Spark','Pandas','Java','Python', 'PHP']
# fee = [25000,20000,15000,15000,18000]
# duration = ['5o Days','35 Days',np.nan,'30 Days', '30 Days']
# discount = [2000,1000,800,500,800]
# columns=['Courses','Fee','Duration','Discount']
# print(list(zip(technologies,fee)))
# df = pd.DataFrame(list(zip(technologies,fee,duration,discount)), columns=columns)
# print(df)
# with pd.ExcelWriter('Courses.xlsx',mode="w") as writer:
#     df.to_excel(writer, sheet_name='Technologies')
#     # df2.to_excel(writer, sheet_name='Schedule')
import time

print ("Start:%s" % time.ctime())
time.sleep( 10)
print ("End:%s" % time.ctime())