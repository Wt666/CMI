import pandas as pd
df=pd.read_csv("/Users/wt/Downloads/sms_registry_20220926.csv")
# print((df["registe_info_json"]))
df1=df["registe_info_json"]
remarks=df1["PRIVATE"]
print(remarks)